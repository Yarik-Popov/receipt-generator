# Local imports
from base import app, db
from models import User, FridgeItem
import models


# 3rd party imports
from flask import request, render_template, redirect


# Create the database
with app.app_context():
    db.create_all()


@app.route('/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        items = models.get_all_fridge_items()
        return render_template('fridge.html', items=items)
    else:
        requested_items = request.form.getlist("items")
        print(requested_items)
        return redirect('/fridge')

@app.route('/add-item')
def add_item():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
