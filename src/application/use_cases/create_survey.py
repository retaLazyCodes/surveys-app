from src.domain.entities.survey import Survey
from src.domain.entities.option import Option
from uuid import uuid4
from datetime import datetime, timedelta
from typing import List


class CreateSurveyUseCase:
    def __init__(self, survey_repo):
        self.survey_repo = survey_repo

    def execute(self, question: str, owner_id, options: List[str], duration_minutes: int = 60):
        now = datetime.utcnow()
        survey = Survey(
            id=uuid4(),
            question=question,
            owner_id=owner_id,
            created_at=now,
            expires_at=now + timedelta(minutes=duration_minutes),
            options=[
                Option(id=uuid4(), survey_id=None, text=opt) for opt in options
            ]
        )

        for opt in survey.options:
            opt.survey_id = survey.id

        self.survey_repo.save(survey)
        return survey
