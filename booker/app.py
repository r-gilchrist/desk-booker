from flask import Flask, request
from flask_restful import Resource, Api
from .utils import database
from .utils import httpResponses

database.ensure_tables_are_created()

app = Flask(__name__)
api = Api(app)


class Desk(Resource):

    def get(self, desk_id):

        bookings = database.get_bookings_by_desk_id(desk_id)

        if len(bookings) == 0:
            return {"msg": f"No bookings for desk {desk_id}!"}, httpResponses.NO_BOOKINGS

        _, dates, _, names = zip(*bookings)

        return {date: {"name": name} for (date, name) in zip(dates, names)}, httpResponses.GET_OK

    def post(self, desk_id):

        data = request.get_json()

        database.add_booking(desk_id, data["name"], data["date"])

        return {}, httpResponses.POST_OK

    def delete(self, desk_id):

        database.delete_bookings(desk_id)

        return {}, httpResponses.DELETE_OK


class Person(Resource):

    def get(self, person):

        bookings = database.get_bookings_by_person(person)

        if len(bookings) == 0:
            return {"msg": f"{person} has no desk bookings!"}, httpResponses.NO_BOOKINGS

        _, dates, desk_ids, _ = zip(*bookings)

        return {date: {"desk_id": desk_id} for (date, desk_id) in zip(dates, desk_ids)}, httpResponses.GET_OK


api.add_resource(Desk, "/desk/<string:desk_id>")
api.add_resource(Person, "/person/<string:person>")


def run():
    app.run(debug=True)
