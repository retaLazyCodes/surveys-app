class FakeSurveyRepository:
    def __init__(self):
        self.saved = []

    def save(self, survey):
        self.saved.append(survey)
