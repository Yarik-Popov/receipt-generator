# Local imports
from base import app, db
from models import User, FridgeItem

# 3rd party imports
from flask import request, render_template


# Create the database
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add_item')
def additempage():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
