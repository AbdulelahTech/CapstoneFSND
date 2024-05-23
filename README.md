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
- Token: [token](eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkE1bTNmeEVzcnhzZkVxbjhwOHZSbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1kcW5tdmQzZG52Nm8xZXkyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjRjOWUzNmZjYWNkY2FhN2ZlMzNiYjgiLCJhdWQiOiJodHRwczovL21vdmllc19hY3RvcnMvIiwiaWF0IjoxNzE2NDUxMjE0LCJleHAiOjE3MTY1Mzc2MTQsInNjb3BlIjoiIiwiYXpwIjoiSzdyOEFGbU9mdVg4Q2VwT0poMks4YkxBeFR3S0hrWjAiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.f_-hU4Beiy1W60q4u7utwbCw4d6Xz2VfJ9SIgSu4fnI5Sz5NP3CHlbrTvOIt0HB1FDrI72UzG-34JuGp44QhV4ZESwwpqCTYgEv0wJyVaawvtQGNzkEjGmjjp4OUQ4ElvbUgE3-5JWfD5bdsld6XB5Ux1IDdvIOEbbwROasso5lVrA6NzQWVkvEZORrJy8mty7SJFXnjFI34tmTcMdFiUwp4vvZ_F3E66CX2k9wOKr0USYCySZqCyT1UnY-C44FJ0TivhYe2eweILgIltd0GdFzmaAOyRX85V-S6kjeugnOoij7B1e-ZczVv62bcpIBHh1TcMK9JKiQpglGOvp_lqA)

**Casting Director**
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
- Token: [token](eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkE1bTNmeEVzcnhzZkVxbjhwOHZSbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1kcW5tdmQzZG52Nm8xZXkyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjRjOWQ3YzRkMWMzNTcyMDZkZTFkMTAiLCJhdWQiOiJodHRwczovL21vdmllc19hY3RvcnMvIiwiaWF0IjoxNzE2NDUxODA4LCJleHAiOjE3MTY1MzgyMDgsInNjb3BlIjoiIiwiYXpwIjoiSzdyOEFGbU9mdVg4Q2VwT0poMks4YkxBeFR3S0hrWjAiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.AFTyJwKEOEwiHbj8EJ_3aOslrGYkfcCHPOHVkrfEh89qm-ZahDp0GNW0EOx8Wnzi_O58XgqGNU3WJsZ-QJ9Hu2oYYcrr6mKFUNuKSQlEHs0XkTrbYBvZSo8QdawyZ6nRN2cTbsn6L6P8bACTomxY-s56BInZR__0Vowt4hGc12r8_7u9Bvt6SmsxvFgPlfzArah07JhDC3eWWwEEgY0EHfY0faeINyZjN_pNzdaYsGVo0jr2C86nFwUkCtB-BtV2tyPqb3SGbWVVHGj_5aAkpXJWeVaCDD3m_r1c9YZ-5sjNXgrXCdBBxVelt9_Q6jEaEvGJx1CnE13Cu_yYqD9upA)

**Casting Assistant**
- Role permissions:
  - ```get:actors	```
  - ```get:actors-detail	```
  - ```get:movies	```
  - ```get:movies-detail	```
- Email: castingassistant@capstone.com 
- Password: CastingAssistant@24
- Token: [token](eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkE1bTNmeEVzcnhzZkVxbjhwOHZSbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1kcW5tdmQzZG52Nm8xZXkyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjQ2MTAzMTRkMWMzNTcyMDZkOGY2YzMiLCJhdWQiOiJodHRwczovL21vdmllc19hY3RvcnMvIiwiaWF0IjoxNzE2NDUyNzU0LCJleHAiOjE3MTY1MzkxNTQsInNjb3BlIjoiIiwiYXpwIjoiSzdyOEFGbU9mdVg4Q2VwT0poMks4YkxBeFR3S0hrWjAiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWwiXX0.gch3W73IaFn2HKrRmw2jpsOQqzfqul__PrRSiSsfPPDOfDqEy7eTe6uMRsyDbzNSA3zN-LN2tuMBmI4_-jp64KRRYp_AT-yU-q8A0OR6wXY_iWXu8VQU1_vtjdWbwQX9moP6zVyckBX8qbTbs20-nStJ_fl_KZd7n4Bl1OUCpduK2yQmQ0A-rtatk56EgtUwulbqZ8i_cQa6QcN7F_q7tfAbespee9lF5IL2rUmPZp4BxgRY7EOyu52x3zrQhXawUeSNFBpuwBqJItAS6doZAXHSENl1fT1bRMVFne5GWXF_33WyKf5A3507qKiN2Iahm4WzUb2sz42efKJ3hqI3dA)

## Postman Collection
You can find a ready postman collection for you to test the app in [here](<Capstone Full Stack Development Production.postman_collection.json>).

## Base URL
```https://capstonefsnd.onrender.com```

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
