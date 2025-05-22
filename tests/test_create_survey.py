from src.application.use_cases.create_survey import CreateSurveyUseCase
from tests.fakes.fake_survey_repo import FakeSurveyRepository
from uuid import uuid4


def test_create_survey_creates_and_saves_survey():
    fake_repo = FakeSurveyRepository()
    use_case = CreateSurveyUseCase(fake_repo)

    owner_id = uuid4()
    question = "¿Cuál es tu lenguaje favorito?"
    options = ["Python", "JavaScript", "C#"]

    survey = use_case.execute(question, owner_id, options)

    assert survey.question == question
    assert survey.owner_id == owner_id
    assert len(survey.options) == 3
    assert all(opt.survey_id == survey.id for opt in survey.options)
    assert survey in fake_repo.saved
