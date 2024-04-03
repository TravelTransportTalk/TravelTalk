import dataclasses
import os
from typing import Dict, Optional

import requests

import json

from webui.common import *

# BASE_URL = os.environ.get("BASE_URL")
BASE_URL = "http://localhost:8080/tt/"

def auth(tg_id: int) -> Optional[UserControllerResp]:
    url = f"{BASE_URL}users/auth"
    request = AuthUserRequest(tg_id)
    json_response = requests.post(url, json=dataclasses.asdict(request))
    if json_response.ok:
        return UserControllerResp.from_json(json_response.content)
    else:
        return None

def register_trip(trip: AddTripRequest):
    url = f"{BASE_URL}trips/add"

    def uuid_to_str(obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
    json_serialized = json.dumps(dataclasses.asdict(trip), default=uuid_to_str)
    json_serialized_single_quotes = json_serialized.replace('"', "'")
    json_response = requests.post(url, json=json_serialized_single_quotes)
    if json_response.ok:
        print(json_response.content)
        return None
        # return AuthUserResponse.from_json(json_response.content)
    else:
        print(json_response)
        return None

def find_trip(filter: Dict) -> List[Trip]:
    url = f"{BASE_URL}trips/find"
    encoded_json = json.dumps(filter)
    requests.post(url, encoded_json)

    user = User(uuid4(), "General_bum", "Эмир Вильданов", "Люблю болтать", "EmirVildanov")

    return [
        Trip(TransportType.TRAIN, datetime.today(), user),
        Trip(TransportType.TRAIN, datetime.today(), user),
        Trip(TransportType.TRAIN, datetime.today(), user),
        Trip(TransportType.TRAIN, datetime.today(), user),
        Trip(TransportType.TRAIN, datetime.today(), user),
    ]

def get_all_stations() -> List[StationShort]:
    url = f"{BASE_URL}stations"
    json_response = requests.get(url)
    if json_response.ok:
        stations = StationShort.schema().loads(json_response.content, many=True)
        return stations
    else:
        return None
