from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for demonstration
users = [
    {"id": 1, "username": "john"},
    {"id": 2, "username": "jane"},
    {"id": 3, "username": "alice"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        if username:
            new_user = {
                'id': len(users) + 1,
                'username': username
            }
            users.append(new_user)
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
