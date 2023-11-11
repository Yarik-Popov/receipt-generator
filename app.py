from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class FridgeItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Foreign key to User table
    input_date = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return '<FridgeItem %r>' % self.name


# Create the database
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'You have submitted a POST request'
    else:
        new_user = User(name='John')
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            print(e)
            return str(e)
        users = User.query.order_by(User.id).all()
        output = ''
        for user in users:
            output += user.name + '<br>'
        return output
    # new_user = User(name='John')
    # try:
    #     db.session.add(new_user)
    #     db.session.commit()
    #     new_item = FridgeItem(name='Milk', expiry_date=datetime.utcnow(), user_id=new_user.id)
    #     db.session.add(new_item)
    #     db.session.commit()
    # except Exception as e:
    #     print(e)
    #     return 'There was an issue adding your user and item'
    # finally:
    #     users = User.query.order_by(User.id).all()
    #     return users


if __name__ == '__main__':
    app.run(debug=True)
