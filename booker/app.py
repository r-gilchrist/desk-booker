from flask import Flask, request
from flask_restful import Resource, Api
from .utils import database
from .utils import httpResponses

database.ensure_tables_are_created()

app = Flask(__name__)
api = Api(app)


class Desk(Resource):

    def get(self, desk_id):

        bookings = database.get_bookings(desk_id)

        if len(bookings) == 0:
            return {"msg": f"No bookings for desk {desk_id}!"}, httpResponses.NO_BOOKINGS

        ids, _, names = zip(*bookings)

        return {id: {"name": name} for (id, name) in zip(ids, names)}, httpResponses.GET_OK

    def post(self, desk_id):

        data = request.get_json()

        database.add_booking(desk_id, data["name"])

        return {}, httpResponses.POST_OK

    def delete(self, desk_id):

        database.delete_bookings(desk_id)

        return {}, httpResponses.DELETE_OK


api.add_resource(Desk, "/desk/<string:desk_id>")


def run():
    app.run(debug=True)
