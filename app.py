from flask import Flask, render_template, request, jsonify, session
from topic import Topic

app = Flask(__name__)
app.secret_key = "a-long-random-unique-string"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        data = request.get_json()
        try:
            if data.get('for') == 'confirmation':
                username = data.get('username')
                password = data.get('password')
                # Here you would typically validate the username and password
                if username == "admin":
                    if password == "password":
                        session["user_id"] = username
                        return jsonify({"status": "success", "message": "Login successful", "redirect": "/admin"})
                    else:
                        return jsonify({"status": "error", "message": "Invalid password"})
                elif password == "password":
                    session["user_id"] = "guest"
                    return jsonify({"status": "success", "message": "Invalid username", "redirect": "/contact"})
                else:
                    return jsonify({"status": "error", "message": "Invalid username and password, Your first time, do you want to sign up?"})


        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/about')
def about():
    return "about page"
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/contact')
def contact():
    return "contact page"
@app.route('/admin/math', methods=['GET', 'POST'])
def math():
    math_topic = Topic("Math")
    if request.method == 'GET':
        return render_template('math.html')
    else:
        data = request.get_json()
        if data.get('command') == 'add_question':
            question_prompt = data.get('question')
            answer = data.get('answer')
            difficulty = data.get('difficulty')
            math_topic.add_questions(question_prompt, answer, difficulty)
            return jsonify({"status": "success", "message": "Question added successfully"})
    if data.get('command') == 'get_question':
        question = math_topic.get_questions()
        if question:
            return jsonify({"status": "success", "question": question.prompt})
        else:
            return jsonify({"status": "error", "message": "No questions available."})
    if data.get('command') == 'submit_answer':
        user_answer = data.get('answer')
        if question and question.check_answer(user_answer):
            return jsonify({"status": "success", "message": "Correct answer!"})
        else:
            return jsonify({"status": "error", "message": "Wrong answer."})
    
        # topic_choice = input("Let's start the quiz! Choose a topic (Math/Science): ")
        # if topic_choice.lower() == "math":
        #     topic = math_topic
        # elif topic_choice.lower() == "science":
        #     topic = science_topic
        # else:
        #     print("Invalid topic choice. Exiting the quiz.")
        #     return
        
        # print ("the question form the topic is :")
        # question = topic.get_questions()
        # print(question.prompt)
        # user_answer = input("Your answer: ")
        # if question.check_answer(user_answer):
        #     print("Correct!")
        # else:
        #     print(f"Wrong! The correct answer is: {question.answer}")

@app.route('/admin/science')
def science():
    if request.method == 'GET':
        return render_template('science.html')

@app.route('/admin/games')
def games():
    return render_template('games.html')

if __name__ == '__main__':
    app.run(debug=True)