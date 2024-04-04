import dataclasses
import os
from typing import Dict, Optional
from uuid import uuid4
import streamlit as st

import requests

import json

from webui.common import *

BASE_URL = os.getenv('API_BASE_URL')

# Helper method to handle UUID serialization.
def uuid_to_str(obj):
    if isinstance(obj, uuid.UUID):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

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

    json_serialized = json.dumps(dataclasses.asdict(trip), default=uuid_to_str)
    # json_serialized = trip.to_json()
    headers = {'Content-type': 'application/json'}
    json_response = requests.post(url, data=json_serialized, headers=headers)
    if json_response.ok:
        print(f"Successfully added trip: {trip}")
    else:
        print(json_response.text)
        print(f"Failed to add trip: {trip}")


def find_trips(filter: FindTripRequest) -> FindTripResponse:
    url = f"{BASE_URL}trips/find"

    json_serialized = filter.to_json()
    headers = {'Content-type': 'application/json'}

    json_response = requests.post(url, data=json_serialized, headers=headers)

    if json_response.ok:
        trip_response = FindTripResponse.from_json(json_response.content)
        return trip_response
    else:
        return None

def get_all_stations() -> List[StationShort]:
    url = f"{BASE_URL}stations"
    json_response = requests.get(url)
    if json_response.ok:
        stations = StationShort.schema().loads(json_response.content, many=True)
        return stations
    else:
        return None


@st.cache_data
def get_stations_by_type(transport_type: TransportType) -> List[StationShort]:
    api_transport_type_name = transport_type_get_api_view(transport_type)
    url = f"{BASE_URL}stations/{api_transport_type_name}"
    json_response = requests.get(url)
    if json_response.ok:
        stations = StationShort.schema().loads(json_response.content, many=True)
        return stations
    else:
        return None

def get_all_transports() -> List[Transport]:
    url = f"{BASE_URL}transports/all"
    json_response = requests.get(url)
    if json_response.ok:
        stations = Transport.schema().loads(json_response.content, many=True)
        return stations
    else:
        return None

def get_transport_by_name(name: str) -> Transport:
    url = f"{BASE_URL}transports/get"
    params = {"name": name}
    json_response = requests.get(url, params=params)
    if json_response.ok:
        return Transport.from_json(json_response.content)
    else:
        return None
