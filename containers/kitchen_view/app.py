from flask import Flask, jsonify, render_template, request
from datetime import datetime
import random
import mysql.connector

# Create flask app
app = Flask(__name__)
orders = [] # All orders info storage


# Home page for KitchenView
@app.route("/")
def index():    
    return render_template("index.html", orders=orders)


# Handeling data recieved
@app.route("/receive_cart", methods=["POST"])
def receive_cart():
    cart = request.get_json()

    if cart:
        # Adjust the order
        order = [
            random.randrange(1000, 9999), # ID
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Time
            [] # Items
        ]
        # Get items from cart
        for item in cart:
            if "order_items" in item:
                order[2].append(item["order_items"])
            if "ingrediens" in item:
                order[2].append(f"{item['choice']}, {item['ingrediens']}")
        orders.append(order)

    print("Received Cart Data")
    return jsonify({"status": "success", "message": "Cart data received"}), 200


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
