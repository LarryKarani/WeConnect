

class User:
    counter=0
    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.id = User.counter=+1
    def reset_password(self, new_password):
        self.password = new_password

        


class Db:
     def __init__(self):
    
         self.user_list=[]
         self.business_list =[]
         self.reviews_list = []

class LoginAttempt:
    def __init__(self, user_name, password):
        self.user_name =user_name
        self.password = password

class Business():
    counter=0
    def __init__(self, busines, category, location, bussines_id):
        self.business = busines
        self.category = category
        self.location = location
        self.id = Business.counter=+1
class Reviews(Business):
    counter =0
    def __init__(self, comments, owner):
        self.comments = comments =+ 1
        self.owner = owner
        self.bussines_id = self.id
        self.id = Reviews.counter

        