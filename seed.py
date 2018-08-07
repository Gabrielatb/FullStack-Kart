from model import Grocery
from model import connect_to_db, db

from sqlalchemy import func
from server import app

#####Grocery Items####
def seed_data():

    cherimoya = Grocery(item_name="cherimoya")
    cherry = Grocery(item_name="cherry")
    pineapple = Grocery(item_name="pineapple")

    pine_nuts = Grocery(item_name="pine nuts")
    almonds = Grocery(item_name="almonds")
    milk = Grocery(item_name="milk")
    almond_milk = Grocery(item_name="almond milk")

    broccoli = Grocery(item_name="broccoli")
    broccolini = Grocery(item_name="pie")
    cherry_pie = Grocery(item_name="cherry pie")
    blueberry_pie = Grocery(item_name="blueberry pie")
    blueberries = Grocery(item_name="blueberries")
    apples = Grocery(item_name="apples")
    apple_pie = Grocery(item_name="apple pie")
    avocado = Grocery(item_name="avocado")
    sugar = Grocery(item_name="sugar")
    bacon = Grocery(item_name="bacon")
    egg = Grocery(item_name="eggs")
    tofu = Grocery(item_name="tofu")
    tofurkey = Grocery(item_name="tofurkey")
    potatoes = Grocery(item_name="potatoes")
    patatoes = Grocery(item_name="patatoes")
    bananas = Grocery(item_name="bananas")
    grapes = Grocery(item_name="grapes")
    grapefruit = Grocery(item_name="grapefruit")
    grapefruit_juice = Grocery(item_name="grapefruit juice")
    grape_juice = Grocery(item_name="grape juice")
    orange_juice = Grocery(item_name="orange juice")
    oranges = Grocery(item_name="oranges")
    orange_bandana = Grocery(item_name="orange bandana")
    orangutan_stuffed_animal = Grocery(item_name="orangutan stuffed animal")
    diapers = Grocery(item_name="diapers")
    tea_tree_shampoo = Grocery(item_name="tea tree shampoo")
    hand_soap = Grocery(item_name="hand soap")
    dishsoap = Grocery(item_name="dishsoap")
    hand_sanitizer = Grocery(item_name="hand sanitizer")
    paper_plates = Grocery(item_name="paper plates")
    paper_towels = Grocery(item_name="paper towels")
    raspberries = Grocery(item_name="raspberries")
    cat_food = Grocery(item_name="cat food")
    tuna_fish = Grocery(item_name="tuna fish")
    kibbles = Grocery(item_name="kibbles")
    English_breakfast_tea = Grocery(item_name="English breakfast tea")
    green_tea = Grocery(item_name="green tea")
    cherry_chapstick = Grocery(item_name="cherry chapstick")
      # "sirloin steak",
      # "New York strip steak",
      # "chicken nuggets",
      # "sparkling water",
      # "coconut water",
      # "coconut flakes",
      # "taco mix",
      # "trailmix",
      # "spam",
      # "beef broth",
      # "chicken soup",
      # "tomato soup",
      # "cherry tomatoes",
      # "beefsteak tomatoes",
      # "sun-dried tomatoes",
      # "sunscreen",
      # "sunblock",
      # "shaving cream",
      # "whipped cream",
      # "creamy tomato soup",
      # "chocolate candy bar",
      # "chocolate-covered cherries",
      # "milk",
      # "chocolate milk",
      # "protein bar",
      # "bar soap",
      # "pickles",
      # "pickled fish",
      # "olive oil",
      # "olives",
      # "coconut oil",
      # "avocado oil",
      # "zucchini",
      # "zuchini",
      # "peanut butter",
      # "almond butter",
      # "peanuts",
      # "macadamia nuts",
      # "butter"

    db.session.add_all([cherimoya, cherry, pineapple, pine_nuts, almonds, milk, almond_milk,
                       broccoli, broccolini, cherry_pie, blueberry_pie, blueberries, apples,
                       apple_pie, avocado,  sugar, bacon, tofu,  tofurkey, potatoes, patatoes, bananas,
                       grapes, grapefruit_juice, grape_juice, orange_juice, oranges,
                       orange_bandana, orangutan_stuffed_animal, diapers, tea_tree_shampoo, hand_soap,
                       dishsoap, hand_sanitizer, paper_plates, paper_towels, raspberries,
                       cat_food, tuna_fish, kibbles, English_breakfast_tea, green_tea,
                       cherry_chapstick, oranges, orange_bandana, orangutan_stuffed_animal,
                       diapers, tea_tree_shampoo, hand_soap,
                       dishsoap,hand_sanitizer, paper_plates, paper_towels, raspberries, cat_food, tuna_fish, kibbles,
                       English_breakfast_tea, green_tea, cherry_chapstick])
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    #Creating tables
    db.create_all()

    #importing data
    seed_data()