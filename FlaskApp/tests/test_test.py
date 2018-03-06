import unittest
from FlaskApp.app import app
import json

class RegisterTestCase(unittest.TestCase):
	def setUp(self):
		self.dummy_client = app.test_client()
		self.dummy_user = {"name":"ames","password":"ame99s","email":"ames@hj"}
		self.dummy_login ={"name":"larry", "password":"rteyuii"}
	def test_return_helloword(self):
		response = self.dummy_client.get('/POST/api/auth/register')
		self.assertEqual(json.loads(response.data)['hello'], 'world')

		#TEST IF THE METHOD REGISTER A USER WHO DOES NOT EXIST

	def test_regesters_new_user(self):
		response = self.dummy_client.post('/POST/api/auth/register',data=json.dumps(self.dummy_user)
		,content_type='application/json')
		self.assertEqual(json.loads(response.data) ,[self.dummy_user])

       #TEST USERNAME THAT ALREADY EXIST DOES NOT REGISTER
       #Email already registered

     #test unsuccessfull_login
	def test_unsuccefull_login(self):
		response =self.dummy_client.post('/POST/api/auth/login', data=json.dumps(self.dummy_login), content_type='application/json')
		self.assertEqual(json.loads(response.data),{"name":"you are not a registered user"})

    #test successfull_login
	def test_logout(self):
		response =self.dummy_client.get('/POST/api/auth/logout')
		self.assertEqual(json.loads(response.data), {"hey":"you are logged out"})

		
		
	



                              