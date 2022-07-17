import requests

BASE_URL = "http://127.0.0.1:5000/desk/"

DATE = "2022-08-01"

VALID_DESKS = [f"S{str(n).zfill(3)}" for n in range(1, 101)]

for desk_id in VALID_DESKS:
    requests.post(BASE_URL + desk_id, json={"name": "unassigned", "date": DATE})
