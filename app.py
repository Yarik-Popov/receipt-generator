# Local imports
from base import app, db
from models import User, FridgeItem
from datetime import datetime


# 3rd party imports
from flask import request, render_template, flash, redirect


# Create the database
with app.app_context():
    db.create_all()
    db.session.add(User(name='Main'))
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add-item')
def add_item():
    return render_template('add.html')

@app .route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    expiry_date = request.form.get('expiry_date')

     # Convert expiry_date from string to datetime object
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
    
    # Create a new FridgeItem instance
    new_item = FridgeItem(name=name, expiry_date=expiry_date, user_id=1)
    db.session.add(new_item)
    db.session.commit()
    flash('New ingredient added successfully!')
    return redirect('/add-item')

if __name__ == '__main__':
    app.run(debug=True)
