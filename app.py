# Local imports
from base import app, db
from models import User, FridgeItem, get_all_fridge_items
from datetime import datetime
from recipe import get_recipes, get_image

# 3rd party imports
from flask import url_for, request, render_template, redirect, flash

# Create the database
with app.app_context():
    db.create_all()
    db.session.add(User(name='Main'))
    db.session.commit()


@app.route('/fridge', methods=['GET'])
def fridge():
    items = get_all_fridge_items()
    return render_template('fridge.html', items=items)
        

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    requested_items = request.form.getlist("items")
    print(requested_items)
    recipe = 'recipe'
    image_url = 'image_url'
    # recipe = get_recipes([], requested_items)  # No seasonings
    # image_url = get_image(recipe)
    return render_template('recipe.html', recipe=recipe, image_url=image_url)


@app.route('/')
def starter():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
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
    return redirect('/fridge')


@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item_to_delete = FridgeItem.query.get(item_id)
    if item_to_delete:
        db.session.delete(item_to_delete)
        db.session.commit()
        flash("Ingredient deleted successfully!")
    else :
        flash("Looks like you tried to delete nothing...")
    return redirect(url_for('fridge'))



if __name__ == '__main__':
    app.run(debug=True)
