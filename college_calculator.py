class CollegeCalculator:
    def __init__(self, colleges):
        self.colleges = colleges
        self.scores = {}
        for college in colleges:
            self.scores[college] = 0


test = CollegeCalculator(['UCLA', 'UCSD'])
print(test.scores)