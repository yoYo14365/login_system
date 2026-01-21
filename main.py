from topic import Topic

def main():


    math_topic = Topic("Math")

    math_topic.add_questions("What is 2 + 2?", "4", "easy")
    math_topic.add_questions("What is the square root of 16?", "4", "medium")
    math_topic.add_questions("What is the derivative of x^2?", "2x", "hard")

    science_topic = Topic("Science")
    science_topic.add_questions("What planet is known as the Red Planet?", "Mars", "easy")
    science_topic.add_questions("What is H2O commonly known as?", "Water", "easy")


    topic_choice = input("Let's start the quiz! Choose a topic (Math/Science): ")
    if topic_choice.lower() == "math":
        topic = math_topic
    elif topic_choice.lower() == "science":
        topic = science_topic
    else:
        print("Invalid topic choice. Exiting the quiz.")
        return
    
    print ("the question form the topic is :")
    question = topic.get_questions()
    print(question.prompt)
    user_answer = input("Your answer: ")
    if question.check_answer(user_answer):
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {question.answer}")
