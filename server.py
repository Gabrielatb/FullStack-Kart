
from flask import Flask, request, render_template, session, redirect, jsonify
import json
import requests
import jinja2
from model import connect_to_db, db, Grocery, Kart



app = Flask(__name__)

json_string = open("items.json").read()
data = json.loads(json_string)

@app.route('/')
def home_page():
    """home page"""

    return render_template("homepage.html")


@app.route("/kart")
def autcomplete():
    """provides list for item searched """


    all_items = Kart.query.all()
    print "PRINTING ALL ITEMS " + str(all_items)
    return render_template("shop.html", all_items=all_items)



@app.route('/suggestions')
def search_results():
#     """Online Shopping Page"""


    items = db.session.query(Grocery.item_name).all()
    available_commodities = []
    for item in items:
        available_commodities.extend(item)
    commodities = sorted(set(available_commodities))
    return jsonify(commodities)
#     keyword = requests.get('keyword')

#     json_string = open("items.json").read()
#     data = json.loads(json_string)
    
#     available_commodities = []

#     for item in data:
#             available_commodities.append(item)

#     commodities = sorted(available_commodities)
#     return jsonify(commodities)


#     return render_template("shop.html", data=data)

@app.route("/kartitem", methods=['POST'])
def add_item():

    item_searched = request.form['item_searched']
    grocery_item = Grocery.query.filter_by(item_name=item_searched).all()
    for item in grocery_item:
        if Kart.query.filter_by(kart_item_id=item.grocery_item_id).all():
            item = Kart.query.filter_by(kart_item_id=item.grocery_item_id).all()
            for i in item:
                i.quantity +=1
        else:
            item_object = Kart(kart_item_id=item.grocery_item_id, quantity=1) 

            db.session.add(item_object)
     
    db.session.commit()
    
    return render_template("shop.html")




if __name__ == "__main__":

    connect_to_db(app)


    app.run(port=5000, host='0.0.0.0', debug=True)
    
    



