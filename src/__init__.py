from flask import Flask, request, jsonify
from flask_restx import Resource, Api

#instanciate app
app = Flask(__name__)
api = Api(app)

# set configuration
app.config.from_object('src.config.DevelopmentConfig')

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong'
        }
    

api.add_resource(Ping, '/ping')