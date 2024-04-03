from uuid import uuid4

from webui.server_communication import *
from datetime import date


if __name__ == "__main__":
    # res = auth(585998)
    # print(res)

    # @dataclass_json
    # @dataclass
    # class T:
    #     id: int
    #     name: str
    # request = T(1, "aba")
    # print(dataclasses.asdict(request))
    # print(json.dumps(dataclasses.asdict(request), default=uuid_to_str))
    # print(json.dumps(dataclasses.asdict(request)))

    today_date = date.today().strftime("%d-%m-%Y")
    now_time = datetime.now().strftime("%H:%M:%S")
    res = register_trip(AddTripRequest(uuid4(), uuid4(), today_date, now_time, "DF789", uuid4(), uuid4()))
    print(res)

    # get_all_stations()
