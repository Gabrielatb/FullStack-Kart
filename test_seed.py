"""File to seed data from model.py"""

from model import Grocery, Kart
from model import connect_to_db, db

from sqlalchemy import func
from server import app


##############################################################################


def test_seed_data():

    """Seeding questions from Question class into database"""

    print "Seed Complete."

    cherimoya = Grocery(item_name="cherimoya")
    cherry = Grocery(item_name="cherry")
    pineapple = Grocery(item_name="pineapple")
    pine_nuts = Grocery(item_name="pine nuts")
 



    cherimoya_kart = Kart(kart_item_id=1, quantity=2)
    cherry_kart = Kart(kart_item_id=2, quantity=3)
    pineapple_kart = Kart(kart_item_id=3, quantity=1)
    pine_nuts_kart = Kart(kart_item_id=4, quantity=4)



    db.session.add_all([cherimoya, cherry, pineapple, pine_nuts, cherimoya_kart,
                        cherry_kart, pineapple_kart, pine_nuts_kart
                        ])



    db.session.commit()

    ##############################################################################
if __name__ == "__main__":
    connect_to_db(app)

    #Creating tables
    db.create_all()

    #importing data
    test_seed_data()