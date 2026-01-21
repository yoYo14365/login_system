class Question:
    def __init__(self, prompt, answer, difficulty):
        self.prompt = prompt
        self.answer = answer
        self.difficulty = difficulty

        self.num_seen = 0
        self.num_correct = 0


    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()