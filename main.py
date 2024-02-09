from flask import Flask
from flask_restful import Api,Resource
import json
from data_models.user import User
from repositories.user_repo import UserRepo


app=Flask(__name__)
api=Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data":"Hello World"}

class UserData(Resource):
    def get(self):
        ur=UserRepo()
        data=ur.getAllData()
        users=[]
        for x in data:
            user=User(*x)
            value={"id":user.id,"userName":user.userName,"userPass":user.userPass,"fullName":user.fullName,
                   "userAddress":user.userAddress,"roleId":user.roleId}           
            users.append(value)
        return value#{"data":"data"}

api.add_resource(HelloWorld,"/helloWorld")
api.add_resource(UserData,"/users")
if __name__=="__main__":
    app.run(debug=True)