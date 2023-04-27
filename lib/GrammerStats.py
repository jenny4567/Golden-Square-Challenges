class GrammarStats:
    def __init__(self):
        self.correct = 0
        self.incorrect = 0

    def check(self, text):
        punctuation = [".", "!", "?"]
        if text[-1] not in punctuation:
            self.incorrect += 1
            return False
        if text[0] != text[0].capitalize():
            self.incorrect += 1
            return False
        else:
            self.correct += 1
            return True

    def percentage_good(self):
        return round((self.correct*100/(self.correct+self.incorrect)))