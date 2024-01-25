from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"
###############################################################

db = SQLAlchemy(app)

############################ TO DO 2 ##############################
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
#################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

@app.route('/add_user', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        # code for handling POST request
        name = request.form.get('name')
        email = request.form.get('email')
        user = User(name=name, email=email)
        try:
            db.session.add(user)
            db.session.commit()
            flash('User added successfully!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash('Email already exists!', 'error')
    else:
        return render_template('add_user.html')

@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET','POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        flash("User not found!", 'error')
        return redirect('/')

    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully!", 'success')
        return redirect('/')
    
    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)