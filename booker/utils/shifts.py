import requests

BASE_URL = "http://127.0.0.1:5000/desk/"

def add_shifts(desk_ids, date):
    for desk_id in desk_ids:
        requests.post(BASE_URL + desk_id, json={"name": "unassigned", "date": date})
