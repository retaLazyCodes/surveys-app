from dataclasses import dataclass, field
from .value_objects import EntityId
from datetime import datetime
from typing import List
from .option import Option


@dataclass
class Survey:
    id: EntityId
    question: str
    owner_id: EntityId
    created_at: datetime
    expires_at: datetime
    options: List[Option] = field(default_factory=list)

    def is_active(self) -> bool:
        now = datetime.utcnow()
        return self.created_at <= now < self.expires_at
