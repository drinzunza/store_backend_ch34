from flask import Flask, abort
from data import me, mock_catalog

import json

app = Flask(__name__) # create a new instance, similar to new Task in JS


@app.get("/")
def home():
    return "Hello World!"


@app.get("/about")
def about():
    return "Sergio Inzunza"


@app.get("/contact/me")
def contact_me():
    return "sinzunza@sdgku.edu"



################################################################
################ API -> JSON ###################################
################################################################



@app.get("/api/developer")
def developer():
    return json.dumps(me) #parse me into a json string



@app.get("/api/developer/address")
def dev_address():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zipcode"]
    # f string
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zipcode"]}'



@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)



# GET /api/catalog/count
# returns the number of products on the list
@app.get("/api/catalog/count")
def count_products():
    count = len(mock_catalog)
    return json.dumps(count)


@app.get("/api/category/<cat>")
def prods_by_category(cat):
    results = []
    for prod in mock_catalog:
        if prod["category"] == cat:
            results.append(prod)
            
    return json.dumps(results)



@app.get('/api/product/<id>')
def prod_by_id(id):
    for prod in mock_catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    # not found
    return abort(404, "Invalid id")



@app.get("/api/product/search/<text>")
def search_product(text):
    results = []
    for prod in mock_catalog:
        if text.lower() in prod["title"].lower():
            results.append(prod)

    return json.dumps(results)



@app.get("/api/categories")
def get_categories():
    results = []
    for prod in mock_catalog:
        cat = prod["category"]
        if cat not in results:
            results.append(cat)

    return json.dumps(results)
        



# get /api/total
# should return the sum of all prices

@app.get("/api/total")
def get_total():
    total = 0
    for prod in mock_catalog:
        total += prod["price"]

    return json.dumps(total)


# get /api/cheaper/<price>
# return all the products (list) with price lower or equal to <price>
# note: price will be an string
@app.get("/api/cheaper/<price>")
def get_cheaper(price):
    price = float(price)
    results = []
    for prod in mock_catalog:
        if prod["price"] <= price:
            results.append(prod)

    return json.dumps(results)




# challenge
# find and return the cheapest product

# create a cheapest = mock_catalog[0]
# for loop to travel the list
# get every prod from the list
# if the price of prod is lower than the price of cheapest
# then update cheapest to be the prod (cheapest = prod)





app.run(debug=True)