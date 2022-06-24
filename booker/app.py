from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Desk(Resource):

    def get(self):
        return {}, 200

    def post(self):
        return {}, 201

    def delete(self):
        return {}, 202

api.add_resource(Desk, "/desk")

def run():
    app.run(debug=True)
