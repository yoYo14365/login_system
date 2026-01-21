import random
from question import Question

class Topic:
    def __init__(self, name):
        self.name = name
        self.questions = []


    def add_questions(self, prompt, answer, difficulty):
        question = Question(prompt, answer, difficulty)
        self.questions.append(question)

    def get_questions(self):
        return self.questions[random.randint(0, len(self.questions) - 1)]
