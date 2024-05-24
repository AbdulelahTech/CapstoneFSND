import unittest
from models import setup_test_db, Movies, Actors, db_drop_and_create_all
from app import create_app
import os

class CapstoneTestCase(unittest.TestCase) :
    
  
    @classmethod
    def setUpClass(self):
        """Define test variables and initialize app."""
        self.app = create_app(test_config='testing')
        self.client = self.app.test_client
        db_drop_and_create_all()
        
        self.new_movie = {
            "title": "Test Movie_1",
            "releaseDate": "2023-10-05"
        }
        
        self.new_movie_to_delete = {
            "title": "Test Movie_2",
            "releaseDate": "2023-10-05"
        }
        
        self.new_actor = {
            "name": "Test Actor_1",
            "age": 24,
            "gender": "Male"
        }
        
        self.new_actor_to_delete = {
            "name": "Test Actor_2",
            "age": 30,
            "gender": "Female"
        }
        
        self.executiveProducerAuth = {
            "Authorization": f"Bearer {os.getenv('ExecutiveProducerJWT')}"
        }
        self.CastingDirectorAuth = {
            "Authorization": f"Bearer {os.getenv('CastingDirectorJWT')}"
        }
        self.CastingAssistantAuth = {
            "Authorization": f"Bearer {os.getenv('CastingAssistantJWT')}"
        }

    def tearDown(self):
        """Executed after each test"""
        pass
    
    # Test for Casting Director role
    # Success
    def test_get_all_movies_casting_director(self):
        res = self.client().get('/movies', headers=self.CastingDirectorAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['movies'], list)
    # Failure
    def test_create_new_movie_casting_director(self):
        res = self.client().post('/movies', headers=self.CastingDirectorAuth, json=self.new_movie)
        data = res.get_json()

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
    
    
    # Test for Casting Assistant role
    # Success
    def test_get_all_movies_casting_assistant(self):
        res = self.client().get('/movies', headers=self.CastingAssistantAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['movies'], list)
    # Failure
    def test_create_new_movie_casting_assistant(self):
        res = self.client().post('/movies', headers=self.CastingAssistantAuth, json=self.new_movie)
        data = res.get_json()

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
    
    # Test for Executive Producer role for every route(success/failure)
    # Tests for Movies
    def test_create_new_movie(self):
        res = self.client().post('/movies', headers=self.executiveProducerAuth, json=self.new_movie)
        res = self.client().post('/movies', headers=self.executiveProducerAuth, json=self.new_movie_to_delete)
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data['success'])

    def test_400_if_movie_creation_fails(self):
        # Sending an incomplete request
        res = self.client().post('/movies', headers=self.executiveProducerAuth, json={"title": "Incomplete"})
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
    
    def test_get_specific_movie(self):
        res = self.client().get('/movies/1', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie']['id'], 1)

    def test_404_if_movie_not_found(self):
        # Requesting a non-existent movie id
        res = self.client().get('/movies/1000', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
    
    def test_get_all_movies(self):
        res = self.client().get('/movies', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['movies'], list)

    # Tests for Actors
    def test_create_new_actor(self):
        res = self.client().post('/actors', headers=self.executiveProducerAuth, json=self.new_actor)
        res = self.client().post('/actors', headers=self.executiveProducerAuth, json=self.new_actor_to_delete)
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data['success'])

    def test_400_if_actor_creation_fails(self):
        # Sending an incomplete request
        res = self.client().post('/actors', headers=self.executiveProducerAuth, json={"name": "Missing Age and Gender"})
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_get_specific_actor(self):
        res = self.client().get('/actors/1', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['actor'])
        self.assertEqual(data['actor']['id'], 1)

    def test_404_if_actor_not_found(self):
        # Requesting a non-existent actor id
        res = self.client().get('/actors/1000', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
    
    def test_get_all_actors(self):
        res = self.client().get('/actors', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['actors'], list)

    def test_update_movie(self):
        update = {"title": "Updated Movie Title"}
        res = self.client().patch('/movies/1', headers=self.executiveProducerAuth, json=update)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_404_if_movie_does_not_exist_to_update(self):
        update = {"title": "Nonexistent Movie"}
        res = self.client().patch('/movies/9999', headers=self.executiveProducerAuth, json=update)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
    
    def test_update_movie(self):
        movie = {'title': 'Updated Title'}
        res = self.client().patch('/movies/1', headers=self.executiveProducerAuth, json=movie)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('updated', data)

    def test_404_update_movie_not_found(self):
        res = self.client().patch('/movies/999', headers=self.executiveProducerAuth, json={"title": "No Such Movie"})
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_update_actor(self):
        actor = {'name': 'Updated Actor Name'}
        res = self.client().patch('/actors/1', headers=self.executiveProducerAuth, json=actor)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('updated', data)

    def test_404_update_actor_not_found(self):
        res = self.client().patch('/actors/999', headers=self.executiveProducerAuth, json={"name": "No Such Actor"})
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    # Delete Tests
    def test_delete_movie(self):
        res = self.client().delete('/movies/2', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('deleted', data)

    def test_404_delete_movie_not_found(self):
        res = self.client().delete('/movies/999', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_delete_actor(self):
        res = self.client().delete('/actors/2', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('deleted', data)

    def test_404_delete_actor_not_found(self):
        res = self.client().delete('/actors/999', headers=self.executiveProducerAuth)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

if __name__ == "__main__":
    unittest.main()
