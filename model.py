from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Grocery(db.Model):

    __tablename__ = 'groceryitems'

    grocery_item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_name = db.Column(db.String(250), nullable=False)

    def __repr__(self):

        """Represent grocery item """

        return "<grocery_item_id={} item_name={}>".format(

            self.grocery_item_id, self.item_name)


class Kart(db.Model):

    __tablename__ = 'kart'

    kart_item_id = db.Column(db.Integer,  db.ForeignKey('groceryitems.grocery_item_id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)


    # Define relationship to grocery
    groceryitems = db.relationship("Grocery",
                           backref=db.backref("kart"))

    def __repr__(self):

        """Represent grocery item """

        return "<grocery_item_id={} item_quantity={}".format(

            self.kart_item_id, self.quantity)




##############################################################################

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///grocerydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app

    connect_to_db(app)
    db.create_all()

    print "Connected to DB."
