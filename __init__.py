import os

# os.path.abspath(os.path.dirname(__file__))

from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

import jwt
from flask import jsonify, request
from kwanso_task.config import Config
import kwanso_task.config as config

app = Flask(__name__)
app.config.from_object(config.Config)

api = Api(app)
db = SQLAlchemy(app)

from kwanso_task.resources.user import RegisterUser, GetUser, LoginUser, CreateTask,TaskList

api.add_resource(RegisterUser, '/register', methods=["POST"])
api.add_resource(LoginUser, '/login', methods=["POST"])
api.add_resource(GetUser, '/user', methods=["GET"])
api.add_resource(CreateTask, '/create-task', methods=["POST"])
api.add_resource(TaskList, '/list-tasks', methods=["GET"])


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The requested URL could not be found.</p>", 404




if __name__ == "__main__":
    app.run(port=5000, debug=True)
