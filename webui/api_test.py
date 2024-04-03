from uuid import uuid4
import time

from webui.server_communication import *
from datetime import date


if __name__ == "__main__":
    today_date = date.today().strftime("%d-%m-%Y")
    now_time = datetime.now().strftime("%H:%M:%S+05:00")
    station_short = StationShort("a", "b", "c", "d")
    transport = Transport(uuid4(), "my_transport")
    user = User(uuid4(), "GeneralBum", "Эмир Вильданов", "Люблю гулять", 42, "GeneralBum")
    trip_dto = TripDto(uuid4(), station_short, station_short, today_date, now_time, "code", transport, user)
    find_trip_req = FindTripResponse("a", [trip_dto])
    transport_id = uuid.UUID("91e10f0d-a92c-49f5-b922-dec1e41f7b19")
    user_id = uuid.UUID("04fc2d16-98d4-44dd-ad79-6442fe1bdffc")
    add_trip_request = AddTripRequest("s9807439", "s9807439", today_date, now_time, "DF789", transport_id, user_id)

    # auth(1)
    # StationShort(station_code='s9807439', transport_type='bus', short_name='Касторное, центр', long_name='Касторное, центр, Касторное, Курская область')
    # res = get_all_stations()
    # res = get_stations_by_type(TransportType.WATER)
    # register_trip(add_trip_request)
    # res = find_trips(FindTripRequest())

    # res = get_all_transports()
    res = get_transport_by_name("bus")
    print(res)
