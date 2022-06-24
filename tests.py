import unittest
import requests
import os
from booker.utils.database import ensure_tables_are_created, FILENAME

BASE_URL = "http://127.0.0.1:5000/desk/"


def get(desk_id="S001"):
    '''Sends GET request'''
    response = requests.get(BASE_URL + desk_id)
    return response


def post(desk_id="S001", name="Ryan"):
    '''Sends POST request'''
    response = requests.post(BASE_URL + desk_id, json={"name": name})
    return response


def delete(desk_id="S001"):
    '''Sends DELETE request'''
    response = requests.delete(BASE_URL + desk_id)
    return response


def delete_database():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)


class GetDeskTests(unittest.TestCase):

    def setUp(self) -> None:
        delete_database()
        ensure_tables_are_created()

    def test_get_success_one(self):
        post()
        response = get()
        expectedJSON = {"1": {"name": "Ryan"}}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expectedJSON)

    def test_get_success_two(self):
        post()
        post(name="Sarah")
        response = get()
        expectedJSON = {"1": {"name": "Ryan"}, "2": {"name": "Sarah"}}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expectedJSON)

    def test_get_success_none(self):
        response = get()
        expectedJSON = {"msg": "No bookings for desk S001!"}
        self.assertEqual(response.status_code, 203)
        self.assertEqual(response.json(), expectedJSON)
