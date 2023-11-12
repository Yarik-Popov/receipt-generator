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


@app.route('/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        items = get_all_fridge_items()
        return render_template('fridge.html', items=items)
    else:
        requested_items = request.form.getlist("items")
        recipe = get_recipes([], requested_items)  # No seasonings
        image_url = get_image(recipe)
        return render_template('recipe.html', recipe=recipe, image_url=image_url)


@app.route('/')
def starter():
    return render_template('index.html')


@app.route('/add_item')
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
    return redirect('/add_item')


@app.route('/cooking', methods=['GET','POST'])
def cooking():
    if request.method == 'GET':
        items = get_all_fridge_items()
        return render_template('cooking.html', items=items)
    else:
        requested_items = request.form.getlist("items")
        recipe = get_recipes([], requested_items)  # No seasonings
        image_url = get_image(recipe)
        return render_template('recipe.html', recipe=recipe, image_url=image_url)



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
