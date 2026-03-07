from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return 'Hello'

@app.route('/home')
def home():
    return 'home'

@app.route('/clg')
def clg():
    return 'CLG'

@app.route('/dynamic', defaults={'user_input': 'Guest'})
@app.route('/dynamic/<user_input>')
def dynamic(user_input):
    return f'This is dynamic route: {user_input}'

@app.route('/query')
def query():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Name: {name}, Age: {age}'

# Form → Save to DB
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        new_user = User(name=user_input)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))

    return "<form method='POST' action='/form'><input type='text' name='user_input'/><input type='submit'></form>"

@app.route('/json', methods=['POST'])
def accept_json():
    json_data = request.get_json()
    age = json_data['age']
    return {"age": age}



def insert_data():
    new_user = User(name='Bala', date_joined=datetime.utcnow())
    db.session.add(new_user)
    db.session.commit()


def update_first_user():
    user = User.query.first()   # get first record
    user.name = 'Bidya'
    db.session.commit()
    # if user:
    #     user.name = "Updated Name"
    #     user.date_joined = datetime.utcnow()
    #     db.session.commit()
    #     print("User updated successfully")
    # else:
    #     print("No user found")



if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # creates db.sqlite3 and tables
    app.run(debug=True)