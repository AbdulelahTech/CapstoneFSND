import unittest
from models import setup_test_db, Movies, Actors, db_drop_and_create_all
from app import create_app

class CapstoneTestCase(unittest.TestCase) :
    
  
    @classmethod
    def setUpClass(self):
        """Define test variables and initialize app."""
        self.app = create_app(test_config='testing')
        self.client = self.app.test_client
        
        
        db_drop_and_create_all()
        
        # Binds the app to the current context
        # with self.app.app_context():
        # db_drop_and_create_all()  # reset the database for each test run

        self.new_movie = {
            "title": "Test Movie",
            "releaseDate": "2023-10-05"
        }
        
        self.new_actor = {
            "name": "Test Actor",
            "age": 30,
            "gender": "Female"
        }
        
        self.headers = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkE1bTNmeEVzcnhzZkVxbjhwOHZSbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1kcW5tdmQzZG52Nm8xZXkyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjRjOWUzNmZjYWNkY2FhN2ZlMzNiYjgiLCJhdWQiOiJodHRwczovL21vdmllc19hY3RvcnMvIiwiaWF0IjoxNzE2Mjk3MzAwLCJleHAiOjE3MTYzODM3MDAsInNjb3BlIjoiIiwiYXpwIjoiSzdyOEFGbU9mdVg4Q2VwT0poMks4YkxBeFR3S0hrWjAiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.QYiKLTGcnnei533q9jnnYmoGzKFqn57RoPeb9FfTApPo4gVaJI0Rg6iUKciDgO5a2ApImo_DnAeJupmgNSL2j9JxPC_ZB-wpYN2Akk-GMBgF5-obCC3T2IvIC1NdtWY3EptcvQd3355X2ZLVMZfGt-MWumyCNPTxoN2oDD6VDuxdkNtLPPzl0yOh1IXbiGGLyFO8gzj2517H1m6eH5tRm0JR9iqLku3AKPEjX_UFZYCpoKjrpNrdL94GtGjCCvejYYcaqtSFBu5qcCUZlylMl4ujuPXKwE3E31umoLFEi06Bfs113KYjCsYHe4TO2D7zjHP3M0b-lb5y0KTYxKUaQg"
        }

    def tearDown(self):
        """Executed after each test"""
        pass
    
    
    
    # Tests for success and error case of POST /movies
    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.headers)
        data = res.get_json()
        print("data-2")
        print(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertTrue(data['success'])
    
    # Tests for success and error case of GET /movies
    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.headers)
        data = res.get_json()
        print("data")
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']) >= 0)
    

if __name__ == "__main__":
    unittest.main()
