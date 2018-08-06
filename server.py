
from flask import Flask, request, render_template, session, redirect
import jinja2



app = Flask(__name__)


@app.route('/')
def home_page():
    """home page"""

    return render_template("homepage.html")

@app.route('/shop')
def shop():
    """Online Shopping Page"""

    return render_template("shop.html")

               
    

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)