from dataclasses import dataclass
from .value_objects.entity_id import EntityId


@dataclass
class User:
    id: EntityId
    email: str
    name: str
