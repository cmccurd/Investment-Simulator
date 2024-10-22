from app import create_app
from flask import (Flask, render_template)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/add_user')
def add_user():
    try:
        new_user = User(username='jd', email='jd@example.com')
        db.session.add(new_user)
        db.session.commit()
        return 'User added!'
    except Exception as e:
        return str(e)  # Return the error message for debugging

@app.route('/users')
def users():
    users = User.query.all()  # Fetch all users from the database
    return ', '.join([user.username for user in users])
