class CodeGradingModel:
    def _init_(self, keywords):
        self.keywords = keywords

    def grade(self, code):
        score = sum(1 for keyword in self.keywords if keyword in code)
        return score / len(self.keywords)