from dataclasses import dataclass
from .value_objects.entity_id import EntityId


@dataclass
class Option:
    id: EntityId
    survey_id: EntityId
    text: str
