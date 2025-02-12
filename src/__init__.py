from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app)

# set config
app.config.from_object('src.config.DevelopmentConfig')


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'ping pong.......!'
        }
    
api.add_resource(Ping, '/ping')