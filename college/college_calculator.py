class CollegeCalculator:
    def __init__(self, colleges):
        self.colleges = colleges
        self.scores = {}
        for college in colleges:
            self.scores[college] = 0

    def major(self, college):
        score = 0
        good = ['y', 'jh', 'ucla', 't', 'hm', 'wu', 'slo', 'uci', 'ucsd', 'u', 'cwr', 'ucr', 'p', 'lb', 'ucsc']
        if college == 'p':
            score += 6
        if college in ['jh', 'ucla', 't', 'uci', 'ucsd', 'cwr', 'lb']:
            score += 5
        if college in ['wu', 'slo', 'u', 'ucr', 'ucsc']:
            score += 4
        if college == 'y':
            score += 3
        if college == 'hm':
            score += 2
        if college == 'nyu':
            score += 1
        if college in good:
            score *= 10
        self.scores[college] += score

    def politics(self, college):
        score = 0
        good = ['y', 'jh', 'ucla', 't', 'hm', 'wu', 'ucsd', 'nyu', 'cwr', 'ucr', 'lb', 'ucsc']
        if college in ['y', 'jh', 'ucla', 'wu', 'nyu', 'ucr', 'lb', 'ucsc']:
            score += 4
        if college in ['t', 'hm', 'ucsd', 'cwr']:
            score += 3
        if college in ['slo', 'uci', 'u']:
            score += 2
        if college == 'p':
            score += 1
        if college in good:
            score *= 9
        self.scores[college] += score

    def housing(self, college):
        score = 0
        good = ['y', 'jh', 'ucla', 't', 'hm', 'wu', 'slo', 'uci', 'nyu', 'p', 'ucsc']
        if college in good:
            score += 2
        if college in ['ucsd', 'u', 'cwr', 'ucr', 'lb']:
            score += 1
        if college in good:
            score *= 8
        self.scores[college] += score

    def ratio(self, college):
        score = 0
        good = ['y', 'jh', 't', 'hm', 'nyu', 'u']
        if college in ['y', 'jh']:
            score += 10
        if college in ['hm', 'nyu']:
            score += 9
        if college in ['t', 'u']:
            score += 8
        if college in ['wu', 'cwr']:
            score += 7
        if college == 'p':
            score += 6
        if college in ['ucla', 'uci']:
            score += 5
        if college in ['slo', 'ucsd']:
            score += 4
        if college == 'lb':
            score += 3
        if college == 'ucr':
            score += 2
        if college == 'ucsc':
            score += 1
        if college in good:
            score *= 5
        self.scores[college] += score

    def location(self, college):
        score = 0
        good = ['y', 'jh', 'ucla', 't', 'hm', 'wu', 'slo', 'uci', 'ucsd', 'nyu', 'u', 'ucr', 'p', 'lb', 'ucsc']
        if college in good:
            score += 2
        if college == 'cwr':
            score += 1
        if college in good:
            score *= 4
        self.scores[college] += score

    def cost(self, college):
        score = 0
        good = ['ucla', 'slo', 'uci', 'ucsd', 'ucr', 'lb', 'ucsc']
        if college == 'lb':
            score += 11
        if college == 'slo':
            score += 10
        if college in ['ucla', 'uci']:
            score += 9
        if college in ['ucsd', 'ucr', 'ucsc']:
            score += 8
        if college == 'p':
            score += 7
        if college == 'cwr':
            score += 6
        if college in ['jh', 'nyu']:
            score += 5
        if college in ['y', 'wu']:
            score += 4
        if college == 'hm':
            score += 3
        if college == 'u':
            score += 2
        if college == 't':
            score += 1
        if college in good:
            score *= 3
        self.scores[college] += score

    def system(self, college):
        score = 0
        good = ['y', 'jh', 't', 'hm', 'wu', 'slo', 'nyu', 'u', 'cwr', 'p', 'lb']
        if college in good:
            score += 2
        if college in ['ucla', 'uci', 'ucsd', 'ucr', 'ucsc']:
            score += 1
        if college in good:
            score *= 6
        self.scores[college] += score

    def athletics(self, college):
        score = 0
        good = ['jh', 't', 'hm', 'wu', 'nyu', 'cwr', 'ucsc']
        if college in good:
            score += 2
        if college in ['y', 'ucla', 'slo', 'uci', 'ucsd', 'u', 'ucr', 'p', 'lb']:
            score += 1
        if college in good:
            score *= 2
        self.scores[college] += score


    def vibe(self, college):
        score = 0
        good = ['y', 'jh', 'ucla', 'hm', 'wu', 'slo', 'uci', 'ucsd', 'u', 'cwr', 'lb']
        if college in good:
            score += 2
        if college in ['t', 'nyu', 'ucr', 'p', 'ucsc']:
            score += 1
        if college in good:
            score *= 7
        self.scores[college] += score

    



    def run(self):
        for college in self.colleges:
            self.major(college)
            self.politics(college)
            self.housing(college)
            self.ratio(college)
            self.location(college)
            self.cost(college)
            self.system(college)
            self.athletics(college)
            self.vibe(college)
            
        


calc = CollegeCalculator(['uci', 'u', 'cwr', 'ucr', 'p'])
calc.run()
print(calc.scores)