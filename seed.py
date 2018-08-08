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
    sirloin_steak = Grocery(item_name="sirloin steak")
    New_York_strip_steak = Grocery(item_name="New York strip steak")
    chicken_nuggets = Grocery(item_name="chicken nuggets")
    sparkling_water = Grocery(item_name="sparkling water")
    coconut_water = Grocery(item_name="coconut water")
    coconut_flakes = Grocery(item_name="coconut flakes")
    taco_mix = Grocery(item_name="taco mix")
    trail_mix = Grocery(item_name="trailmix")
    spam = Grocery(item_name="spam")
    beef_broth = Grocery(item_name="beef broth")
    chicken_soup = Grocery(item_name="chicken soup")
    tomato_soup = Grocery(item_name="tomato soup")
    cherry_tomatoes = Grocery(item_name="cherry tomatoes")
    beefsteak_tomatoes = Grocery(item_name="beefsteak tomatoes")
    sun_dried_tomatoes = Grocery(item_name="sun-dried tomatoes")
    sunblock_sunscreen = Grocery(item_name="sunscreen")
    sunblock = Grocery(item_name="sunblock")
    shaving_cream = Grocery(item_name="shaving cream")
    whipped_cream = Grocery(item_name="whipped cream")
    creamy_tomato_soup = Grocery(item_name="creamy tomato soup")
    chocolate_candy_bar = Grocery(item_name="chocolate candy bar")
    chocolate_covered_cherries = Grocery(item_name="chocolate-covered cherries")
    milk = Grocery(item_name="milk")
    chocolate_milk = Grocery(item_name="chocolate milk")
    protein_bar = Grocery(item_name="protein bar")
    bar_soap = Grocery(item_name="bar soap")
    pickles = Grocery(item_name="pickles")
    pickled_fish = Grocery(item_name="pickled fish")
    olive_oil = Grocery(item_name="olive oil")
    olives = Grocery(item_name="olives")
    coconut_oil = Grocery(item_name="coconut oil")
    avocado_oil = Grocery(item_name="avocado oil")
    zucchini = Grocery(item_name="zucchini")
    zuchini = Grocery(item_name="zuchini")
    peanut_butter = Grocery(item_name="peanut butter")
    almond_butter = Grocery(item_name="almond butter")
    peanuts = Grocery(item_name="peanuts")
    macadamia_nuts = Grocery(item_name="macadamia nuts")
    butter = Grocery(item_name="butter")

    db.session.add_all([cherimoya, cherry, pineapple, pine_nuts, almonds, milk, almond_milk,
                       broccoli, broccolini, cherry_pie, blueberry_pie, blueberries, apples,
                       apple_pie, avocado,  sugar, bacon, tofu,  tofurkey, potatoes, patatoes, bananas,
                       grapes, grapefruit_juice, grape_juice, orange_juice, oranges,
                       orange_bandana, orangutan_stuffed_animal, diapers, tea_tree_shampoo, hand_soap,
                       dishsoap, hand_sanitizer, paper_plates, paper_towels, raspberries,
                       cat_food, tuna_fish, kibbles, English_breakfast_tea, green_tea,
                       cherry_chapstick, oranges, orange_bandana, orangutan_stuffed_animal,
                       diapers, tea_tree_shampoo, hand_soap, dishsoap, hand_sanitizer, paper_plates,
                       paper_towels, raspberries, cat_food, tuna_fish, kibbles,
                       English_breakfast_tea, green_tea, cherry_chapstick, sirloin_steak,
                        New_York_strip_steak, chicken_nuggets , sparkling_water, coconut_water, coconut_flakes,
                        taco_mix ,trail_mix, spam, beef_broth ,chicken_soup tomato_soup,
                        cherry_tomatoes,beefsteak_tomatoes ,sun_dried_tomatoes ,sunblock_sunscreen ,sunblock,
                        shaving_cream, whipped_cream ,creamy_tomato_soup ,chocolate_candy_bar ,
                        chocolate_covered_cherries ,milk ,chocolate_milk ,protein_bar,bar_soap ,
                        pickles, pickled_fish ,olive_oil ,olives ,coconut_oil ,avocado_oil ,zucchini ,zuchini,peanut_butter,
                        almond_butter, peanuts, macadamia_nuts, butter])








    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    #Creating tables
    db.create_all()

    #importing data
    seed_data()