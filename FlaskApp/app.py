from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

user_list = [ ]


@app.errorhandler(404)
def page_not_found():
	return jsonify({"error": "resource not found"})

# api 
class register_user(Resource):
	def get (self):
		return {'hello': 'world'}, 200

	def post(self):
		if len(user_list)!=0:
			for user in user_list:
				if user["name"]==request.json["name"]:
					return {"name":"already exist"}

				elif user["email"] == request.json["email"]:
					return {"email":"already in use"}

		new_user = {
				 	"name":request.json["name"],
					"email":request.json["email"],
					"password":request.json["password"]
					}

		user_list.append(new_user)

		return user_list

api.add_resource(register_user, '/POST/api/auth/register')


class login(Resource):
	def get (self):
		return {'page': 'loads'}, 200

	def post(self):
		for user in user_list:

			if user["name"]!=request.json["name"] and user["password"]!=request.json["password"]:
				return {"name":"you are not a registered user"}

		return {"name":"you are logged in"}
	
api.add_resource(login, '/POST/api/auth/login')

class logout(Resource):
	def get(self):
		return {'hey':'you are logged out'}, 200

api.add_resource(logout, '/POST/api/auth/logout')



if __name__ == '__main__':
	app.run(debug=True)