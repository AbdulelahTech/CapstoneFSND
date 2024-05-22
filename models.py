import os
from dotenv import load_dotenv
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json

# TODO: uncomment this line to use a local database
# load_dotenv()

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_test_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('test_database_path')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('database_path')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


# Association table for the many-to-many relationship between Moviess and Actorss
movies_actors_association = Table('Movies_Actors', db.Model.metadata,
                                  Column('Movies_id', Integer, ForeignKey(
                                      'Movies.id'), primary_key=True),
                                  Column('Actors_id', Integer, ForeignKey(
                                      'Actors.id'), primary_key=True)
                                  )

'''
Movies
a persistent Movies entity, extends the base SQLAlchemy Model
'''


class Movies(db.Model):
    __tablename__ = 'Movies'

    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String Title
    title = Column(String(80), unique=True)
    releaseDate = Column(Date(), nullable=False)
    actors = relationship(
        'Actors', secondary=movies_actors_association, back_populates='movies')

    '''
    short()
        short form representation of the Movies model
    '''

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'releaseDate': self.releaseDate.strftime('%Y-%m-%d'),
        }

    '''
    long()
        long form representation of the Movies model
    '''

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'releaseDate': self.releaseDate.strftime('%Y-%m-%d'),
            'Actors': [actor.name for actor in self.actors]
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            Movies = Movies(title=req_title, recipe=req_recipe)
            Movies.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            Movies = Movies(title=req_title, recipe=req_recipe)
            Movies.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            Movies = Movies.query.filter(Movies.id == id).one_or_none()
            Movies.title = 'Black Coffee'
            Movies.update()
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
    

class Actors(db.Model):
    __tablename__ = 'Actors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    movies = relationship('Movies', secondary=movies_actors_association, back_populates='actors')

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'Movies': [movie.title for movie in self.movies]
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())