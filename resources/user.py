from flask_restful import Resource, reqparse, request, output_json
from kwanso_task.models.user import db, User, Task
from flask import jsonify, json
from kwanso_task.config import Config
import jwt


def auth_check():
    token = None

    if 'Authorization' in request.headers:
        token = request.headers["Authorization"]

    if not token:
        return output_json(code=400, data={'message': 'a valid token is missing'})

    try:
        data = jwt.decode(token.split()[-1], Config.SECRET_KEY, algorithms="HS256")
        return data
    except:
        return jsonify({'message': 'token is invalid'})


class RegisterUser(Resource):

    def post(self):
        data = json.loads(request.data)
        if not data.keys().__contains__("email"):
            return output_json(code=400, data={'message': "Email is not provided."})
        if not data.keys().__contains__("password"):
            return output_json(code=400, data={'message': "Password is not provided."})
        email = data["email"]
        password = data["password"]
        user = User(email, password)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(email=email).first()
        return output_json(code=200, data={"user": user.get()})


class LoginUser(Resource):

    def post(self):
        data = json.loads(request.data)
        if not data.keys().__contains__("email"):
            return output_json(code=400, data={'message': "Email is not provided."})
        if not data.keys().__contains__("password"):
            return output_json(code=400, data={'message': "Password is not provided."})
        email = data["email"]
        password = data["password"]
        user = User.query.filter_by(email=email).first()
        if user.verify_password(password):
            return output_json(code=200, data=jwt.encode({"email": email}, Config.SECRET_KEY, algorithm="HS256"))


class GetUser(Resource):
    def get(self):
        result = auth_check()
        if type(result) == dict:
            user = User.query.filter_by(email=result["email"]).first()
            return output_json(code=200, data={"user": user.get()})
        else:
            return result


class CreateTask(Resource):
    def post(self):
        result = auth_check()
        if type(result) == dict:
            data = json.loads(request.data)
            if not data.keys().__contains__("name"):
                return output_json(code=400, data={'message': "Task name is not provided."})
            name = data["name"]
            task = Task(name)
            db.session.add(task)
            db.session.commit()
            task = Task.query.filter_by(name=name).first()
            return output_json(code=200, data={"task": task.get()})
        else:
            return result


class TaskList(Resource):
    def get(self):
        result = auth_check()
        if type(result) == dict:
            tasks = Task.query.all()
            result = {"tasks": []}
            for key in tasks:
                result["tasks"].append(key.get())
            return output_json(code=200, data=result)
        else:
            return result
