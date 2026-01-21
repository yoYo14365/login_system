from flask import Flask, render_template, request, jsonify, session

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
@app.route('/admin/math')
def math():
    return render_template('math.html')

@app.route('/admin/science')
def science():
    return render_template('science.html')

@app.route('/admin/games')
def games():
    return render_template('games.html')

if __name__ == '__main__':
    app.run(debug=True)