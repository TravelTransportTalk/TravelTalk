import uuid
from typing import List
from enum import Enum
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from datetime import datetime


class TransportType(Enum):
    TRAIN = 1,
    AIRPLANE = 2

def get_available_transport_types() -> List[TransportType]:
    return [TransportType.TRAIN, TransportType.AIRPLANE]

def transport_type_get_readable_view(type: TransportType) -> str:
    match type:
        case TransportType.TRAIN:
            formatted = "Поезд"
        case TransportType.AIRPLANE:
            formatted = "Самолёт"
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
    fromId: uuid.UUID
    toId: uuid.UUID
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
    to_location: Location = field(metadata=config(field_name="to"))