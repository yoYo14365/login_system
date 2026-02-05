import random
from question import Question

class Topic:
    def __init__(self, name):
        self.name = name
        self.questions = []


    def add_questions(self, prompt, answer, difficulty):
        question = Question(prompt, answer, difficulty)
        self.questions.append(question)
        self.questions.sort(key=lambda q: q.difficulty)
        print(f"Question added: {prompt} with difficulty {difficulty}")

    def get_questions(self):
        if not self.questions:
            print("No questions available.")
            return None
        return self.questions[random.randint(0, len(self.questions) - 1)]
