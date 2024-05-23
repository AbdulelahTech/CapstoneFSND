# Movie Casting API Documentation
**Submitted by:** Abdulelah Alzoman

## Overview
This Flask application provides a backend API for managing movies and actors for a casting agency. It supports operations such as retrieving, adding, updating, and deleting movie and actor records, with appropriate authorization checks in place.

## Technologies Used
- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-CORS

## Development Setup
1. Clone the repository to your local machine.
2. Ensure Python 3.8.x is installed.
3. Install project dependencies by running `pip install -r requirements.txt`.
4. Set up your database and update the database URI in [.env](./.env).
5. Run the application using `python app.py`.

## JWT tokens
To obtain a JWT token for a specifc role please go to [this login page](https://dev-dqnmvd3dnv6o1ey2.us.auth0.com/authorize?audience=https://movies_actors/&response_type=token&client_id=K7r8AFmOfuX8CepOJh2K8bLAxTwKHkZ0&redirect_uri=https://127.0.0.1:8080/login-result), then sign in with desired user as bellow:

**Executive Producer**

- Email: executiveproducer@capstone.com 
- Password: ExecutiveProducer@24
- Token: [token](eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkE1bTNmeEVzcnhzZkVxbjhwOHZSbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1kcW5tdmQzZG52Nm8xZXkyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjRjOWUzNmZjYWNkY2FhN2ZlMzNiYjgiLCJhdWQiOiJodHRwczovL21vdmllc19hY3RvcnMvIiwiaWF0IjoxNzE2NDUxMjE0LCJleHAiOjE3MTY1Mzc2MTQsInNjb3BlIjoiIiwiYXpwIjoiSzdyOEFGbU9mdVg4Q2VwT0poMks4YkxBeFR3S0hrWjAiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.f_-hU4Beiy1W60q4u7utwbCw4d6Xz2VfJ9SIgSu4fnI5Sz5NP3CHlbrTvOIt0HB1FDrI72UzG-34JuGp44QhV4ZESwwpqCTYgEv0wJyVaawvtQGNzkEjGmjjp4OUQ4ElvbUgE3-5JWfD5bdsld6XB5Ux1IDdvIOEbbwROasso5lVrA6NzQWVkvEZORrJy8mty7SJFXnjFI34tmTcMdFiUwp4vvZ_F3E66CX2k9wOKr0USYCySZqCyT1UnY-C44FJ0TivhYe2eweILgIltd0GdFzmaAOyRX85V-S6kjeugnOoij7B1e-ZczVv62bcpIBHh1TcMK9JKiQpglGOvp_lqA)

**Casting Director**

- Email: castingdirector@capstone.com 
- Password: CastingDirector@24

**Casting Assistant**

- Email: castingassistant@capstone.com 
- Password: CastingAssistant@24
## API Endpoints

### Movies
- **GET** `/movies`  
  Retrieves a list of all movies. Requires `get:movies` permission.
  
- **GET** `/movies/<int:movie_id>`  
  Retrieves the details of a specific movie by ID. Requires `get:movies-detail` permission.
  
- **POST** `/movies`  
  Creates a new movie with the provided title and release date. Requires `post:movies` permission.
  
- **PATCH** `/movies/<int:movie_id>`  
  Updates an existing movie specified by ID. Can update the title, release date, and associated actors. Requires `patch:movies` permission.
  
- **DELETE** `/movies/<int:movie_id>`  
  Deletes a movie specified by ID. Requires `delete:movies` permission.

### Actors
- **GET** `/actors`  
  Retrieves a list of all actors. Requires `get:actors` permission.
  
- **GET** `/actors/<int:actor_id>`  
  Retrieves the details of a specific actor by ID. Requires `get:actors-detail` permission.
  
- **POST** `/actors`  
  Creates a new actor with the provided name, age, and gender. Requires `post:actors` permission.
  
- **PATCH** `/actors/<int:actor_id>`  
  Updates an existing actor specified by ID. Can update the name, age, gender, and associated movies. Requires `patch:actors` permission.
  
- **DELETE** `/actors/<int:actor_id>`  
  Deletes an actor specified by ID. Requires `delete:actors` permission.

### Error Handling
Errors are returned as JSON objects in the following format:
```json
{
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```
