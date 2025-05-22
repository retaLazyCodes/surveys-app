from dataclasses import dataclass
from .value_objects import EntityId


@dataclass
class User:
    id: EntityId
    email: str
    name: str
