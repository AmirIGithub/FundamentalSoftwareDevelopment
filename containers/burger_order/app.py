from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import requests

# Create flask app
app = Flask(__name__)
app.secret_key = "secret key"

# Connect to the database
connection = mysql.connector.connect(
    user="root", password="root", host="mysql", port="3306", database="db"
)


# (helper) Fetch data from the database
def fetch_data_from_db(connection, table_name):
    cur = connection.cursor()
    query = f"SELECT * FROM {table_name}"
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    return result


# Home page for BurgerOrder
@app.route("/")
def index():

    # create a session cart
    displayable_cart = []
    if "cart" not in session:
        session["cart"] = []
    # make the cart list displayable
    else:
        for item in session["cart"]:
            if "order_items" in item:
                displayable_cart.append(item["order_items"])

    # Get data from the database
    menu_items = fetch_data_from_db(connection, "menu_items")
    hamburger_items = fetch_data_from_db(connection, "hamburger_items")
    chickenAndFish_items = fetch_data_from_db(connection, "chickenAndFish_items")
    vegitarian_items = fetch_data_from_db(connection, "vegitarian_items")
    friesAndSides_items = fetch_data_from_db(connection, "friesAndSides_items")
    beverages_items = fetch_data_from_db(connection, "beverages_items")
    desserts_items = fetch_data_from_db(connection, "desserts_items")
    ingredients_items = fetch_data_from_db(connection, "ingredients_items")
    orders = fetch_data_from_db(connection, "orders")
    
    return render_template("index.html", menu_items=menu_items, hamburger_items=hamburger_items, chickenAndFish_items=chickenAndFish_items, vegitarian_items=vegitarian_items,friesAndSides_items=friesAndSides_items,beverages_items=beverages_items, desserts_items=desserts_items,ingredients_items=ingredients_items, orders=orders, cart=displayable_cart)


# Add to cart, handeling
@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    item = request.form
    if item:
        session["cart"].append(item)
    session.modified = True
    return redirect(url_for("index"))


# Handleing place order
@app.route("/place_order")
def place_order():
    # Send cart data to kitchen view
    try:
        response = requests.post(
            "http://kitchen_view:5000/receive_cart",
            json=session["cart"]
        )
        print("Response from kitchen view:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error sending cart data:", e)
    # reset cart
    session["cart"] = []
    session.modified = True
    return redirect(url_for("index"))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

