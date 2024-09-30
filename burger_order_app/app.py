from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Add your MySQL password if necessary
app.config['MYSQL_DB'] = 'MenuStore'

# Initialize MySQL
mysql = MySQL(app)

# Route for Burger Order Page
@app.route('/')
def burger_order():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM menu_items")
    menu_items = cur.fetchall()
    
    cur.execute("SELECT * FROM hamburger_items")
    hamburger_items = cur.fetchall()
    
    cur.execute("SELECT * FROM chickenAndFish_items")
    chickenAndFish_items = cur.fetchall()
    
    cur.execute("SELECT * FROM vegitarian_items")
    vegitarian_items = cur.fetchall()
    
    cur.execute("SELECT * FROM friesAndSides_items")
    friesAndSides_items = cur.fetchall()
    
    cur.execute("SELECT * FROM beverages_items")
    beverages_items = cur.fetchall()
    
    cur.execute("SELECT * FROM desserts_items")
    desserts_items = cur.fetchall()
    
    cur.execute("SELECT * FROM ingredients_items")
    ingredients_items = cur.fetchall()
    
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    
    cur.execute("SELECT * FROM cart")
    cart = cur.fetchall()
    
    cur.close()
    return render_template('burger_order.html', menu_items=menu_items, hamburger_items=hamburger_items, chickenAndFish_items=chickenAndFish_items, vegitarian_items=vegitarian_items,friesAndSides_items=friesAndSides_items,beverages_items=beverages_items, desserts_items=desserts_items,ingredients_items=ingredients_items, orders=orders, cart=cart)


# Route to handle order submission
# Route to handle order submission
@app.route('/submit_order', methods=['POST'])
def submit_order():
    if request.method == 'POST':
        selected_items = request.form.getlist('order_items')
        selected_items += request.form.getlist('choice')
        selected_items += request.form.getlist('ingrediens')
        if selected_items:
            order_details = ', '.join(selected_items)
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO cart (order_details) VALUES (%s)", [order_details])
            mysql.connection.commit()
            cur.close()
        return redirect('/')

# Route for Kitchen View Page
@app.route('/kitchen')
def kitchen_view():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO orders (order_details, order_time) SELECT order_details, order_time FROM cart")
    cur.execute("TRUNCATE TABLE cart")
    cur.execute("SELECT * FROM orders ORDER BY order_time DESC")
    orders = cur.fetchall()
    cur.close()
    return render_template('kitchen_view.html', orders=orders)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

