import unittest

from server import app
import server

from model import db, Grocery, Kart

from test_seed import test_seed_data


def connect_to_db(app):
    """Connecting the database to our Flask Application"""
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///testdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

class Homepage(unittest.TestCase):
        "confirming homepage is as expected"

        def setUp(self):
            """Todo before every test"""

            self.client = app.test_client()
            app.config['TESTING'] = True
            # Connect to test database
            connect_to_db(app)
            db.create_all()
            test_seed_data()

        def test_home_page(self):
            """Testing homepage"""

            result = self.client.get("/")
            self.assertEqual(result.status_code, 200)
            self.assertIn("<h1 style='color:blue'> Online Shopping made easy! <h1>", result.data)


        def redirect(self):
            """redirects to shop page"""
            result = self.client.get("/kart")
            self.assertEqual(result.status_code, 200)
            self.assertIn("<h1 style='color:blue;text-align:center;margin-top: 5%;'> Add Items to Your Cart </h1>", result.data)

        def tearDown(self):
            """Todo after each test."""

            db.session.close()
            db.drop_all()




class Kart(unittest.TestCase):
    def setUp(self):
        """Todo before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True
        # Connect to test database
        connect_to_db(app)
        db.create_all()


    def add_item(self):
        """Suggestions in search bar"""

        result = self.client.post("/kartitem",
                                  data={'item_searched': "eggs"},
                                    follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("<td>cherimoya</td>", result.data)
        self.assertIn("<td>1</td>", result.data)

    def tearDown(self):
        """Todo after each test."""
        db.session.close()
        db.drop_all()

        




if __name__ == "__main__":
    unittest.main()