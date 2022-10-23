from operator import truediv
from flask import Flask
from flask import request
from flask import abort
import string
import random

from activities import Activities
from mongo import Mongo
from user import User

app = Flask(__name__)


userdb = Mongo()

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/hello')
def good_morning():
    return 'Good Morning'


@app.route('/bye/<name>')
def bye_name(name):
    return 'Bye %s!' % name


@app.route('/signup', methods=['POST'])
def sign_up():
   def check_string(category, user_dict):
      if (category not in user_dict):
         return False

      user_input = user_dict[category]

      if isinstance(user_input, str):
         if (len(user_input) >= 2) and (len(user_input) <= 50):
               return True
         else:
               return False
      else:
         return False

   content = request.get_json()

   if (not check_string("username", content)):
      abort(400, "invalid")
   if (userdb.find(content["username"]) != None):
      abort(400, "user already exists")
   if (not check_string("password", content)):
      abort(400, "invalid")
   if (not check_string("name", content)):
      abort(400, "invalid")
   if (not check_string("groupid", content)):
      abort(400, "invalid")
   if (not check_string("city", content)):
      abort(400, "invalid")
   if (not check_string("state", content)):
      abort(400, "invalid")
   if (not check_string("email", content)):
      abort(400, "invalid")
   if (not check_string("phoneNumber", content)):
      abort(400, "invalid")

   token = ''.join(random.choice(string.ascii_letters + string.digits)
                  for _ in range(64))

   user_activities = Activities(0, 0, 0, 0, 0, 0)

   ret = {
      "status": "success",
      "user": {
         "username": content["username"],
         "password": content["password"],
         "name": content["name"],
         "groupid": content["groupid"],
         "company": "Vanderbilt University",
         "activities": {
               "waterScore": user_activities.waterScore,
               "co2Score": user_activities.co2Score,
               "serviceScore": user_activities.serviceScore,
               "wasteScore": user_activities.serviceScore,
               "impactScore": user_activities.impactScore,
               "numberOfActivities": user_activities.numberOfActivities
         },
         "token": token,
         "city": content["city"],
         "state": content["state"],
         "email": content["email"],
         "phoneNumber": content["phoneNumber"],
      }
   }
   
   print(ret)
   print(ret["user"])
   print(ret["user"]["activities"])
   
   user_info = User.dictToUser(ret["user"])

   userdb.insert(user_info)

   return ret


@app.route('/login', methods=['POST'])
def log_in():
   content = request.get_json()
   if ("username" not in content):
      abort(400, "invalid")
   if ("password" not in content):
      abort(400, "invalid")

   current_user = userdb.find(content["username"])

   if current_user == None:
      abort(400, "invalid username")

   if (content["password"] != current_user.password):
      abort(400, "wrong password")

   ret = {
      "status": "success",
      "user": {
         "username": current_user.username,
         "password": current_user.password,
         "name": current_user.name,
         "groupid": current_user.groupid,
         "company": "Vanderbilt University",
         "activities": {
               "waterScore": current_user.activities["waterScore"],
               "co2Score": current_user.activities["co2Score"],
               "serviceScore": current_user.activities["serviceScore"],
               "wasteScore": current_user.activities["wasteScore"],
               "impactScore": current_user.activities["impactScore"],
               "numberOfActivities": current_user.activities["numberOfActivities"]
         },
         "token": current_user.token,
         "city": current_user.city,
         "state": current_user.state,
         "email": current_user.email,
         "phoneNumber": current_user.phoneNumber,
      }
   }
   return ret

@app.route('/profile', methods = ['GET'])
def profile():
    username = request.args.get("q")
    user = userdb.find(username)
    if user == None:
        abort(400, "user does not exist")
    print("hi")
    dict = user.__dict__
    dict.pop("password")
    dict.pop("token")
    dict.pop("email")
    dict.pop("phoneNumber")
    return dict

@app.route('/leaderboard', methods = ['GET'])
def leaderboard():
   users = userdb.mycol.find()
   userList = []

   for userDict in users:
      userList.append(User.dictToUser(userDict))
   userList.sort(reverse = True)

   returnList = []
   for user1 in userList:
      myDict = user1.__dict__
      myDict.pop("password")
      myDict.pop("token")
      myDict.pop("email")
      myDict.pop("phoneNumber")
      returnList.append(myDict)
   
   print("hi")
   returnDict = {"rankingList" : returnList}
   print(returnDict)
   return returnDict

if __name__ == '__main__':
    app.run()