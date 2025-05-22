from dataclasses import dataclass
from .value_objects.entity_id import EntityId
from datetime import datetime


@dataclass
class Vote:
    id: EntityId
    user_id: EntityId
    survey_id: EntityId
    option_id: EntityId
    voted_at: datetime
