from typing import List
from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid5


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

@dataclass
class Trip:
    uuid: int
    from_location: int
    to_location: int
    date: datetime
    time: str
    transport_type: TransportType
    code: str
    author_id: uuid5


@dataclass
class User:
    id: int
    nick: str
    full_name: str
    description: str
    tg_username: str
