# Movie Casting API Documentation
**Submitted by:** Abdulelah Alzoman

## Overview
This Flask application provides a backend API for managing movies and actors for a casting agency. It supports operations such as retrieving, adding, updating, and deleting movie and actor records, with appropriate authorization checks in place.

## Motivation
This project was created as part of the Udacity Full Stack Web Developer Nanodegree Program, and i hope this **endeavour** made me a better **developer**.

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

## Deployment instruction
1. Sign in to [render](https://dashboard.render.com/).
2. Set up a Database Service with Postgres by clicking **New PostgreSQL**.
3. Then create anthor service called **web service**
4. Click Build and deploy from a Git repository
5. From public repo provide the link of this repo.
6. Then put ```python3 app.py``` as a start command

## JWT tokens
To obtain a JWT token for a specifc role please go to [this login page](https://dev-dqnmvd3dnv6o1ey2.us.auth0.com/authorize?audience=https://movies_actors/&response_type=token&client_id=K7r8AFmOfuX8CepOJh2K8bLAxTwKHkZ0&redirect_uri=https://127.0.0.1:8080/login-result), then sign in with desired user as bellow:

**Executive Producer**
- Description: All permissions a Casting Director has and add or delete a movie from the database
- Role permissions:
  -  ```delete:actors```	
  -  ```delete:movies	```	
  -  ```get:actors```	
  -  ```get:actors-detail```	
  -  ```get:movies```	
  -  ```get:movies-detail```	
  -  ```patch:actors```	
  -  ```patch:movies```	
  -  ```post:actors```	
  -  ```post:movies```	
- Email: executiveproducer@capstone.com 
- Password: ExecutiveProducer@24
- Token: [token](eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkE1bTNmeEVzcnhzZkVxbjhwOHZSbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1kcW5tdmQzZG52Nm8xZXkyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjRjOWUzNmZjYWNkY2FhN2ZlMzNiYjgiLCJhdWQiOiJodHRwczovL21vdmllc19hY3RvcnMvIiwiaWF0IjoxNzE2NjM2Mjc3LCJleHAiOjE3MTY3MjI2NzcsInNjb3BlIjoiIiwiYXpwIjoiSzdyOEFGbU9mdVg4Q2VwT0poMks4YkxBeFR3S0hrWjAiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Bm8dq94B23D1xjop7SDyPkqu4RfZmevA6kf8pUbzVNJ2lsx8TRrGZXb-xN9iEaZ3MPnoozDQ1GBdo3WR-r7fL5Jyyjgw_nu0djepkzxMkswqcqpylc5B2acTt55l96f70XMUMVZU35LJFDlk7mUc_38UOLCSz78a_MazuDaGa8e5etUuHukwoyHDreWsUD6_0MeaQESPhZcPBJZAd2jiBUqHECt_uIRhoQUcXQ81hzobuvzwSL0FYDh6M0D4LNmtV43ZJLstpos98m6uy5Jo194BAGDltO-xvgi9Xk254wqfuYVA2h4yQl22up3-EcpU8zPZnF-h0BG7QzI7btjKAw)

**Casting Director**
- Description: All permissions a Casting Assistant has and add or delete an actor from the database modify actors or movies
- Role permissions:
  - ```delete:actors	```
  - ```get:actors	```
  - ```get:actors-detail	```
  - ```get:movies	```
  - ```get:movies-detail	```
  - ```patch:actors	```
  - ```patch:movies	```
  - ```post:actors	```
- Email: castingdirector@capstone.com 
- Password: CastingDirector@24
- Token: [token](eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkE1bTNmeEVzcnhzZkVxbjhwOHZSbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1kcW5tdmQzZG52Nm8xZXkyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjRjOWQ3YzRkMWMzNTcyMDZkZTFkMTAiLCJhdWQiOiJodHRwczovL21vdmllc19hY3RvcnMvIiwiaWF0IjoxNzE2NjM2NDI3LCJleHAiOjE3MTY3MjI4MjcsInNjb3BlIjoiIiwiYXpwIjoiSzdyOEFGbU9mdVg4Q2VwT0poMks4YkxBeFR3S0hrWjAiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.LKlEszITRuHrBVfiaHEfJ91fA6oXfPvfvRzR4zXB7X1WLf5nhXizrxXdHOYMf5DSoDxUC1Gg5b1I9s6pTZkRBwunS30pDS19ejy-8mP9mSUwsmom72GUEBG3x9u8puNPgn57l0TwCFPgsGRJ63l6dPMok_nu8lliSOzuyh2GHejXl70EdMfJJj099hEjjPEGiYpq1Qy8o387DPG1RAGWWN_dlTEv6uZZHKaDFbMJdjV70fy1i3MDcy7SisNRcMuhnqPXyqtNgSBKmf8fCmZQ-xzu0uQQHZPwEiEnaD4sBq6X9dSHyaLPtyj_h8HKlYQe04NcfElXcmKUpg31XCN-9g)

**Casting Assistant**
- Description: Can view actors and movies.
- Role permissions:
  - ```get:actors	```
  - ```get:actors-detail	```
  - ```get:movies	```
  - ```get:movies-detail	```
- Email: castingassistant@capstone.com 
- Password: CastingAssistant@24
- Token: [token](eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkE1bTNmeEVzcnhzZkVxbjhwOHZSbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1kcW5tdmQzZG52Nm8xZXkyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjQ2MTAzMTRkMWMzNTcyMDZkOGY2YzMiLCJhdWQiOiJodHRwczovL21vdmllc19hY3RvcnMvIiwiaWF0IjoxNzE2NjM2NTI0LCJleHAiOjE3MTY3MjI5MjQsInNjb3BlIjoiIiwiYXpwIjoiSzdyOEFGbU9mdVg4Q2VwT0poMks4YkxBeFR3S0hrWjAiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWwiXX0.im27A-0Hvui8RNvTbEqVsZjeh9PlRYOnU1GCRruI22L35zbcXBilHW_G09V-aDuTowbqoENQEiCOT49aSEsVCuPNm68BZ3SkrHHgIjeM5ibJXcaIqD4odG-2oxBph7Duh1IOtMwzHtXru7BKQ-24inNxpHk7aXuk3Lq52RPes17DtRD2KMbtHazugV1ahjo1bCR22BzJ-Lt6b1XTVx4jLxcT2v1yyNpVgLeuLyFnf7JjNUkrT6WKz50lVFmerTtSJd325kQ_PO6jELMgtAMhSekIO6H7BJ1mtSWI3dNt7u4ECTDAQWaM3EM2SraSBKx-hJXXu0wHbr8T-a8RqIWYwg)

## Postman Collection
You can find a ready postman collection for you to test the app in [here](<Capstone Full Stack Development Production.postman_collection.json>).

## Base URL
```https://capstonefsnd.onrender.com```

## API Endpoints

### Movies
- **GET** `/movies`  
  Retrieves a list of all movies. Requires `get:movies` permission.
```json
  {
    "movies": [
        {
            "id": 1,
            "releaseDate": "2027-07-12",
            "title": "test_movie_322"
        }
    ],
    "success": true
}
```
  
- **GET** `/movies/<int:movie_id>`  
  Retrieves the details of a specific movie by ID. Requires `get:movies-detail` permission.
```json
{
    "movie": {
        "Actors": [],
        "id": 1,
        "releaseDate": "2027-07-12",
        "title": "test_movie_322"
    },
    "success": true
}
```
  
- **POST** `/movies`  
  Creates a new movie with the provided title and release date. Requires `post:movies` permission.
```json
{
    "created": {
        "Actors": [],
        "id": 1,
        "releaseDate": "2027-07-12",
        "title": "test_movie_322"
    },
    "success": true
}
```
  
- **PATCH** `/movies/<int:movie_id>`  
  Updates an existing movie specified by ID. Can update the title, release date, and associated actors. Requires `patch:movies` permission.
```json
{
    "success": true,
    "updated": {
        "Actors": [
            "Abdulelah Alzoman"
        ],
        "id": 1,
        "releaseDate": "2027-07-12",
        "title": "test_movie_322"
    }
}
```
  
- **DELETE** `/movies/<int:movie_id>`  
  Deletes a movie specified by ID. Requires `delete:movies` permission.
```json
{
    "deleted": 2,
    "success": true
}
```

### Actors
- **GET** `/actors`  
  Retrieves a list of all actors. Requires `get:actors` permission.
```json
{
    "actors": [
        {
            "age": 24,
            "gender": "male",
            "id": 1,
            "name": "Abdulelah Alzoman"
        }
    ],
    "success": true
}
```
  
- **GET** `/actors/<int:actor_id>`  
  Retrieves the details of a specific actor by ID. Requires `get:actors-detail` permission.
```json
{
    "actor": {
        "Movies": [
            "test_movie_322"
        ],
        "age": 24,
        "gender": "male",
        "id": 1,
        "name": "Abdulelah Alzoman"
    },
    "success": true
}
```
  
- **POST** `/actors`  
  Creates a new actor with the provided name, age, and gender. Requires `post:actors` permission.
```json
{
    "created": {
        "Movies": [],
        "age": 24,
        "gender": "female",
        "id": 2,
        "name": "test actor"
    },
    "success": true
}
```
  
- **PATCH** `/actors/<int:actor_id>`  
  Updates an existing actor specified by ID. Can update the name, age, gender, and associated movies. Requires `patch:actors` permission.
```json
{
    "success": true,
    "updated": {
        "Movies": [
            "test_movie_322"
        ],
        "age": 28,
        "gender": "male",
        "id": 2,
        "name": "Actor_1"
    }
}
```
  
- **DELETE** `/actors/<int:actor_id>`  
  Deletes an actor specified by ID. Requires `delete:actors` permission.
```json
{
    "deleted": 2,
    "success": true
}
```

### Error Handling
Errors are returned as JSON objects in the following format:
```json
{
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```
