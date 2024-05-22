import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, db_drop_and_create_all, Movies, Actors, db, setup_test_db
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.app_context().push()

    if test_config == "testing":
        print('you are now using \033[1mTesting\033[0m environment')
        setup_test_db(app)
    else:
        print('\033[1mDevlopment\033[0m environment')
        setup_db(app)

    CORS(app, origins='*')
    # create/reset table is db
    # db_drop_and_create_all()

    # Movies Routes

    @app.route('/movies', methods=['GET'])
    @requires_auth("get:movies")
    def get_movies(jwt):
        movies = Movies.query.all()
        return jsonify({
            "success": True,
            "movies": [movie.short() for movie in movies]
        }), 200

    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth("get:movies-detail")
    def get_movie(jwt, movie_id):
        movie = Movies.query.get(movie_id)
        if movie is None:
            abort(404)
        return jsonify({
            "success": True,
            "movie": movie.long()
        }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):
        body = request.get_json()
        new_title = body.get('title', None)
        new_release_date = body.get('releaseDate', None)
        actor_ids = body.get('actor_ids', [])  # List of actor IDs

        if not new_title or not new_release_date:
            abort(400, description="title and releaseDate are required.")

        try:
            movie = Movies(title=new_title, releaseDate=new_release_date)
            for actor_id in actor_ids:
                actor = Actors.query.get(actor_id)
                if actor:
                    movie.actors.append(actor)
                else:
                    abort(404, description=f"Actor with ID {
                        actor_id} does not exist.")
            movie.insert()
            return jsonify({
                "success": True,
                "created": movie.long()
            }), 201
        except Exception as e:
            db.session.rollback()
            abort(422, description=str(e))

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(jwt, movie_id):
        movie = Movies.query.get(movie_id)
        if not movie:
            abort(404)

        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('releaseDate', None)
        # Can be None if not updating actors
        actor_ids = body.get('actor_ids', None)

        if title:
            movie.title = title
        if release_date:
            movie.releaseDate = release_date

        if actor_ids is not None:
            movie.actors = []
            for actor_id in actor_ids:
                actor = Actors.query.get(actor_id)
                if actor:
                    movie.actors.append(actor)
                else:
                    abort(404, description=f"Actor with ID {
                        actor_id} does not exist.")

        try:
            movie.update()
            return jsonify({
                "success": True,
                "updated": movie.long()
            }), 200
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))
        finally:
            db.session.close()

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        movie = Movies.query.get(movie_id)
        if not movie:
            abort(404)

        try:
            movie.delete()
            return jsonify({
                "success": True,
                "deleted": movie_id
            }), 200
        except Exception as e:
            db.session.rollback()
            abort(422, description=str(e))
        finally:
            db.session.close()

    # Actors Routes:

    @app.route('/actors', methods=['GET'])
    @requires_auth("get:actors")
    def get_actors(jwt):
        actors = Actors.query.all()
        return jsonify({
            "success": True,
            "actors": [actor.short() for actor in actors]
        }), 200

    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth("get:actors-detail")
    def get_actor(jwt, actor_id):
        actor = Actors.query.get(actor_id)
        if actor is None:
            abort(404)
        return jsonify({
            "success": True,
            "actor": actor.long()
        }), 200

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(jwt):
        body = request.get_json()
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        movie_ids = body.get('movie_ids', [])  # List of movie IDs

        if not new_name or not new_age or not new_gender:
            abort(400, description="Missing required actor properties.")

        try:
            actor = Actors(name=new_name, age=new_age, gender=new_gender)
            for movie_id in movie_ids:
                movie = Movies.query.get(movie_id)
                if movie:
                    actor.movies.append(movie)
                else:
                    abort(404, description=f"Movie with ID {
                        movie_id} does not exist.")
            actor.insert()
            return jsonify({
                "success": True,
                "created": actor.long()
            }), 201
        except Exception as e:
            db.session.rollback()
            abort(422, description=str(e))

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(jwt, actor_id):
        actor = Actors.query.get(actor_id)
        if not actor:
            abort(404)

        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        # Can be None if not updating movies
        movie_ids = body.get('movie_ids', None)

        if name:
            actor.name = name
        if age is not None:
            actor.age = age
        if gender:
            actor.gender = gender

        if movie_ids is not None:
            actor.movies = []
            for movie_id in movie_ids:
                movie = Movies.query.get(movie_id)
                if movie:
                    actor.movies.append(movie)
                else:
                    abort(404, description=f"Movie with ID {
                        movie_id} does not exist.")

        try:
            actor.update()
            return jsonify({
                "success": True,
                "updated": actor.long()
            }), 200
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))
        finally:
            db.session.close()

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        actor = Actors.query.get(actor_id)
        if not actor:
            abort(404)

        try:
            actor.delete()
            return jsonify({
                "success": True,
                "deleted": actor_id
            }), 200
        except Exception as e:
            db.session.rollback()
            abort(422, description=str(e))
        finally:
            db.session.close()

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": f"Unprocessable {error}"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": error.description
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": error.description
        }), 400

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(AuthError)
    def unauthorized(error: AuthError):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
