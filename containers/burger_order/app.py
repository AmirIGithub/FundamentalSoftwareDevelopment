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

# Function to initialize the database
def init_db():
    with app.app_context():  # Ensure application context is active
        cur = mysql.connection.cursor()

        # Create tables
        cur.execute('''
            CREATE TABLE IF NOT EXISTS menu_items(
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS hamburger_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS chickenAndFish_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS vegitarian_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS friesAndSides_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS beverages_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS desserts_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS ingredients_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                order_details TEXT NOT NULL,
                order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS cart (
                id INT AUTO_INCREMENT PRIMARY KEY,
                order_details TEXT NOT NULL,
                order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        # Insert default menu items (only if the tables are empty)
        cur.execute("SELECT COUNT(*) FROM menu_items")
        if cur.fetchone()[0] == 0:  # If the menu_items table is empty
            cur.execute('''
                INSERT INTO menu_items (item_name) VALUES
                ('Hamburgers'),
                ('Chicken and Fish'),
                ('Vegetarian'),
                ('Fries and Sides'),
                ('Beverages'),
                ('Desserts');
            ''')

            cur.execute('''
                INSERT INTO hamburger_items (item_name) VALUES
                ('Honey Mustard'),
                ('Double Honey Mustard'),
                ('Tasty'),
                ('Double Tasty'),
                ('Tasty Bacon'),
                ('Double Tasty Bacon'),
                ('Big Mac'),
                ('Tasty Cheese'),
                ('McDouble'),
                ('Tripple Cheeseburger'),
                ('Cheeseburger'),
                ('Double Cheeseburger'),
                ('Double QP Cheese'),
                ('Hamburger'),
                ('McFeast'),
                ('QP Cheese');
            ''')

            cur.execute('''
                INSERT INTO chickenAndFish_items (item_name) VALUES
                ('McCrispy'),
                ('McCrispy Spicy'),
                ('Tasty Chicken Burger'),
                ('Chicken Salad'),
                ('Chicken Burger'),
                ('McNuggets'),
                ('Hot Wings'),
                ('Fillet-O-Fish');
            ''')

            cur.execute('''
                INSERT INTO vegitarian_items (item_name) VALUES
                ('Veggie Honey Mustard'),
                ('Veggie Tasty'),
                ('Veggie Clubhouse'),
                ('McVegan');
            ''')

            cur.execute('''
                INSERT INTO friesAndSides_items (item_name) VALUES
                ('Fries'),
                ('Chili Cheese Tops'),
                ('Mini Carrots'),
                ('Apples');
            ''')

            cur.execute('''
                INSERT INTO beverages_items (item_name) VALUES
                ('Coca-Cola'),
                ('Coca-Cola Zero'),
                ('Fanta'),
                ('Fanta Exotic'),
                ('Sprite Zero'),
                ('Milkshake Bluberry'),
                ('Milkshake Strawberry'),
                ('Milkshake Vanilla'),
                ('Milkshake Chocolate'),
                ('Coffe'),
                ('Hot Chocolate'),
                ('Tea, Earl Gray');
            ''')

            cur.execute('''
                INSERT INTO desserts_items (item_name) VALUES
                ('McFlurry Oreo'),
                ('McFlurry Daim'),
                ('Sundae Chocolate'),
                ('Sundae Natural'),
                ('Sundae Caramel'),
                ('Triplet Chocolate Cookie'),
                ('McDonut Chocolate'),
                ('Apple Pie');
            ''')

            cur.execute('''
                INSERT INTO ingredients_items (item_name) VALUES
                ('Soft Bun'),
                ('Gluten-free Bun'),
                ('Beef Burger'),
                ('Chicken Burger'),
                ('Bacon'),
                ('Cheese'),
                ('Lettuce'),
                ('Onion'),
                ('Tomato'),
                ('Red Onion'),
                ('Ice');
            ''')

        mysql.connection.commit()
        cur.close()

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


@app.route('/initdb')
def initialize_database():
    init_db()
    return "Database initialized!"

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
    # Ensure the database is initialized within the application context
    with app.app_context():
        init_db()
    app.run(debug=True)
