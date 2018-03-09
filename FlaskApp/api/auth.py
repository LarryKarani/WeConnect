import re
from flask import request
import json
from flask_restful import Resource

try:
    from WeConnect.FlaskApp.model import User, Db, LoginAttempt, Business, Reviews
except Exception:
    from FlaskApp.model import User, Db, LoginAttempt, Business, Reviews

app_db = Db()

class RegisterUser(Resource):
    
    def get (self):
        return {'hello': 'world'}, 200

    #register a new user if he does not exist
    def post(self):
        #check if a user already exist
        email = request.json["email"]
        name = request.json["name"]
        password =request.json["password"]
        for users in app_db.user_list:
            if users.user_name == name:
                return {"user name" :"already exist"}, 400
            elif users.email == email:
                return{"email":"already registered"}, 400

        if len(name)==0:
            return {"please":"enter your name"}, 400

        elif len(email)==0:
            return {"please":"enter your email"}, 400
    

        elif not email.endswith(".com") or "@" not in email:
            return {"please":"enter a valid email"}

        #regex checks if a string contains special chars
        elif not re.match("^[a-zA-Z0-9_]*$", name):
            return {"user name":"should not contain special chars"}, 400
        #add user to Db
        else:
            new_user = User(name,password,email)
            app_db.user_list.append(new_user)
            return {"successfully":"registered"}, 201

class Login(Resource):
    
    def post(self):
        email_t = request.json["email"]
        password_t = request.json["password"]
        if len(email_t)==0:
            return {"please":"enter email"}

        #check if a user exist
        for user in app_db.user_list:
            if user.email != email_t or user.password != password_t:
                return {"invalid":"email or password"}, 400

        else:
            return {"login":"successful"}, 201
    
class Logout(Resource):
    def get(self):
        return {'successfully':'logged out'}, 200

class PasswordReset(Resource):
    def post(self):
        old_password = request.json["old_password"]
        new_password = request.json["new_password"]
        user_email = request.json["user_email"]
        for user in app_db.user_list:
            if user.password == old_password and user.email==user_email:
                user.reset_password(new_password)
                return {"password":"succefully changed"}, 201
            
        else:
            return {"details":"does not match"}, 400


class RegisterBusiness(Resource):
    def post(self):
    #check if user is regestered
        email_u = request.json["email"]
        bussines_name  = request.json["bussines_name"]
        bussines_loc = request.json["bussines_loc"]
        bussines_cat = request.json["bussines_cat"]
        for user in app_db.user_list:
            if user.email == email_u:
                #create an instance of the class
                 
                 new_biz = Business(bussines_name,bussines_cat,bussines_loc,bussines_cat)
                 app_db.business_list.append(new_biz)
                 return {"bussines":"succefuly created"}, 201

        else:
            return {"Only":"Regestered Users can create biz"}, 400
           
                
class UpdateBusiness(Resource):
    def put(self):

        business_id = request.jason["businessId"]
        #detaist to be updated
        category = request.json["category"]
        location = request.json["location"]
        business = request.json["business"]
    
        for business in app_db.business_list:
            if business.id != business_id:

                return {"bussiness":"Does not exit"}, 400
        else:
            business.category = category
            business.location = location
            business. business = business
            return {"business": "business succefull added"}, 201






class DeleteBusiness(Resource):
    def Delete(self):
        business_id = request.json["businessId"]
        for business in app_db.business_list:
            if business.id != business_id:
                return {"business":"does not exits"}, 400
        else:
            app_db.business_list.remove(business)
            return {"business":"succefuly deleted"},204
                
        
class RetrieveOne(Resource):
    def get(self):
        for business in app_db.business_list:
            if business["id"] == request.json["id"]:
                return business
        else:
            return {"business":"does not exist"}, 400

class RetrieveAllBusiness(Resource):
    def get(self):
        return app_db.business_list , 200

class AddReview(Resource):
    def post(self):
        business_id = request.json["bussinesId"]
        comments = request.json["comments"]
        owner_email = request.json["email"]

        for user in app_db.user_list:
            if user.email != owner_email:
                return {"you must":"be regestered first"}
        else:
            new_comment = Reviews(business_id,comments ,owner_email)
            app_db.reviews_list[new_comment]
            return {"comment" :"successfully added"}

    def get(self):
        query_id = request.json["bussinesId"]
        for reviews in app_db.reviews_list:
            if reviews.business_id != query_id:
                return {"business":"does not exist"}
        else:
            return reviews
        




