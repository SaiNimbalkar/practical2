from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Handle form submission
@app.route('/register', methods=['POST'])
def register():
    data = request.form

    user_data = {
        "name": data.get('fullname'),
        "email": data.get('email'),
        "phone": data.get('phone'),
        "course": data.get('course'),
        "country": data.get('country')
    }

    print("User Registered:", user_data)

    return jsonify({"message": "Registration Successful!", "data": user_data})

if __name__ == '__main__':
    app.run(debug=True)