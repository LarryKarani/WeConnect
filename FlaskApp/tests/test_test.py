import unittest
import json

from WeConnect.FlaskApp.app import create_app
from WeConnect.FlaskApp.model import Db, User
from WeConnect.FlaskApp.api.auth import app_db
#config the app with the testing environment
app = create_app('testing')


class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.dummy_client = app.test_client()
        self.dummy_user = {"email":"la@g.com","name":"larry","password":"67890"}
        self.no_name = {"email":"l@g.com","name":"","password":"67890"}
        self.no_email = {"email":" ", "name":"lay","password":"56690"}
        self.login_no_email ={"email":"", "password":"67kjl"}
        self.login_no_pass = {"email":"larry@gmil.com" ,"password":""}
        self.dummy_biz = {"email":"la@gm.com", "bussines_name":"KTDA", "bussines_loc":"india","bussines_cat":"transport"}
        
        
    #test if the end points loads correctly
    def test_page_loads_correctly(self):
        response = self.dummy_client.get('/api/v1/auth/register')
        self.assertEqual(json.loads(response.data), {'hello':'world'})
    #test user regestered successfully
    
    def test_regesters_users(self):
        response = self.dummy_client.post('/api/v1/auth/register',
        data=json.dumps(self.dummy_user),content_type='application/json')
        self.assertEqual(json.loads(response.data), {'successfully':'registered'})
    
    #test empty name field
    def test_empty_namefield(self):
        response = self.dummy_client.post('/api/v1/auth/register',
        data=json.dumps(self.no_name),content_type='application/json')
        self.assertEqual(json.loads(response.data), {"please":"enter your name"})

    #test empty email field
    
    def test_empty_emailfield(self):
        response = self.dummy_client.post('/api/v1/auth/register',
        data=json.dumps(self.no_email),content_type='application/json')
        self.assertEqual(json.loads(response.data), {"please":"enter a valid email"})


      
   
    #test empty email when login
    def test_empty_email(self):
        response = self.dummy_client.post('/api/auth/v1/login',
        data=json.dumps(self.login_no_email),content_type='application/json')
        self.assertEqual(json.loads(response.data),{"please":"enter email"})

    #test regester business for unregestered users
    def test_regester_business(self):
        response = self.dummy_client.post('/api/businesses',
        data=json.dumps(self.dummy_biz),content_type='application/json')
        self.assertEqual(json.loads(response.data),{"Only":"Regestered Users can create biz"})
    #test retrieves a list of all business
    def test_retrieve_business(self):
        response = self.dummy_client.get('/api/businesses/')
        self.assertEqual(json.loads(response.data),[])

    def test_add_review(self):

