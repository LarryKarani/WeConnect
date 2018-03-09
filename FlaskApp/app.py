import json
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

try:
    from WeConnect.FlaskApp.config import config
except Exception:
    from FlaskApp.config import config


try:
    from WeConnect.FlaskApp.api.auth  import RegisterUser, Login, Logout,PasswordReset, RegisterBusiness,UpdateBusiness, DeleteBusiness, RetrieveAllBusiness, RetrieveOne,AddReview
except Exception:
    from FlaskApp.api.auth import RegisterUser,RetrieveOne, Login, Logout,PasswordReset,RegisterBusiness, UpdateBusiness,DeleteBusiness, RetrieveAllBusiness, AddReview


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api = Api(app)

    #regester urls here
    
    api.add_resource(RegisterUser, '/api/v1/auth/register')
    api.add_resource(Login, '/api/auth/v1/login')
    api.add_resource(Logout, '/api/auth/v1/logout')
    api.add_resource( PasswordReset, '/api/auth/reset-password')
    api.add_resource(RegisterBusiness , '/api/businesses')
    api.add_resource(UpdateBusiness , '/api/businesses/<businessId>')
    api.add_resource(DeleteBusiness , '/api/businesses/<businessId>')
    api.add_resource(RetrieveAllBusiness , '/api/businesses/')
    api.add_resource(RetrieveOne , '/api/businesses/<businessId>')
    api.add_resource(AddReview, '/api/businesses/<businessId>/reviews')
    
    
    


    return app




