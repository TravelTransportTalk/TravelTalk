import uuid
from typing import List, Optional
from enum import Enum
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from datetime import datetime


class TransportType(Enum):
    TRAIN = 1, # train
    PLANE = 2, # plane
    BUS = 3,   # bus
    WATER = 4, # water

def get_available_transport_types() -> List[TransportType]:
    return [TransportType.TRAIN, TransportType.PLANE, TransportType.BUS, TransportType.WATER]

def transport_type_get_readable_view(type: TransportType) -> str:
    match type:
        case TransportType.TRAIN:
            formatted = "Поезд"
        case TransportType.PLANE:
            formatted = "Самолёт"
        case TransportType.BUS:
            formatted = "Автобус"
        case TransportType.WATER:
            formatted = "Морское судно"
    return formatted

def transport_type_get_api_view(type: TransportType) -> str:
    match type:
        case TransportType.TRAIN:
            formatted = "train"
        case TransportType.PLANE:
            formatted = "plane"
        case TransportType.BUS:
            formatted = "bus"
        case TransportType.WATER:
            formatted = "water"
    return formatted


class PathType(Enum):
    CODE = 1,
    FROM_TO = 2

def get_available_path_types() -> List[PathType]:
    return [PathType.CODE, PathType.FROM_TO]

def path_type_get_readable_view(type: PathType) -> str:
    match type:
        case PathType.CODE:
            formatted = "Указать номер рейса"
        case PathType.FROM_TO:
            formatted = "Указать пункты ОТПРАВЛЕНИЯ и ПРИБЫТИЯ"
    return formatted


@dataclass
class StationIdNamePair:
    id: str
    name: str

def station_id_name_pair_get_readable_view(pair: StationIdNamePair) -> str:
    return pair.name

def get_available_locations() -> List[str]:
    # TODO: call backend
    return ["Москва", "Санкт-Петербург", "Пермь", "Когалым",
            "Сочи", "Калининград", "Сургут", "Тюмень"
            "Стамбул", "Тбилиси", "Ереван", "Баку", "Рига",
            "Екатеринбург", "Нижний Новгород", "Уфа", "Новосибирск",
            "Омск", "Челябинск"]


@dataclass_json
@dataclass
class User:
    id: uuid.UUID
    nick: str
    fullName: str
    description: str
    tgId: int
    tgUsername: str

@dataclass_json
@dataclass
class AuthUserRequest:
    tgId: int

@dataclass_json
@dataclass
class UserControllerResp:
    message: str
    user: User

@dataclass_json
@dataclass
class AddTripRequest:
    fromId: str
    toId: str
    date: str
    time: str
    code: str
    transportId: uuid.UUID
    authorId: uuid.UUID

@dataclass_json
@dataclass
class Location:
    id: uuid.UUID
    name: str

@dataclass_json
@dataclass
class Transport:
    id: uuid.UUID
    name: str

@dataclass_json
@dataclass
class FindTripRequest:
    fromId: Optional[uuid.UUID] = None
    toId: Optional[uuid.UUID] = None
    date: Optional[str] = None
    time: Optional[str] = None
    code: Optional[str] = None
    transportId: Optional[uuid.UUID] = None
    authorId: Optional[uuid.UUID] = None

@dataclass_json
@dataclass
class Trip:
    id: uuid.UUID
    from_location: Location = field(metadata=config(field_name="from"))
    to_location: Location = field(metadata=config(field_name="to"))
    date: datetime
    time: datetime
    code: str
    transport: Transport
    authorId: User

@dataclass_json
@dataclass
class StationShort:
    station_code: str
    transport_type: str
    short_name: str
    long_name: str

@dataclass_json
@dataclass
class TripDto:
    id: uuid.UUID
    from_location: StationShort = field(metadata=config(field_name="from"))
    to_location: StationShort = field(metadata=config(field_name="to"))
    date: str
    time: str
    code: str
    transport: Transport
    authorId: User

@dataclass_json
@dataclass
class FindTripResponse:
    message: str
    trips: List[TripDto]
