# Local imports
from base import app, db
from models import User, FridgeItem
import models
from recipe import get_recipes, get_image


# 3rd party imports
from flask import request, render_template, redirect


# Create the database
with app.app_context():
    db.create_all()


@app.route('/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        items = models.get_all_fridge_items()
        return render_template('fridge.html', items=items, recipes=None)
    else:
        requested_items = request.form.getlist("items")
        recipe = get_recipes([], requested_items)  # No seasonings
        image_url = get_image(recipe)
        return render_template('recipe.html', recipe=recipe, image_url=image_url)


@app.route('/add-item')
def add_item():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
