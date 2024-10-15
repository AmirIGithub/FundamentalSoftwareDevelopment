-- CREATE DATABASE db;
use db;

-- Table for menu items (e.g., burgers, drinks, etc.)
CREATE TABLE menu_items(
     id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
);


CREATE TABLE hamburger_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
   );
   
   CREATE TABLE chickenAndFish_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
   );

   CREATE TABLE vegitarian_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
   );
   
   CREATE TABLE friesAndSides_items(
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
   );
   
	CREATE TABLE beverages_items(
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
   );
   
   CREATE TABLE desserts_items(
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
   );
   
   
	CREATE TABLE ingredients_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL
   );

-- Table for storing orders
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_details TEXT NOT NULL,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some example menu items
INSERT INTO menu_items (item_name) VALUES
('Hamburgers'),
('Chicken and Fish'),
('Vegetarian'),
('Fries and Sides'),
('Beverages'),
('Desserts');

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

INSERT INTO chickenAndFish_items (item_name) VALUES
('McCrispy'),
('McCrispy Spicy'),
('Tasty Chicken Burger'),
('Chicken Salad'),
('Chicken Burger'),
('McNuggets'),
('Hot Wings'),
('Fillet-O-Fish');

INSERT INTO vegitarian_items (item_name) VALUES
('Veggie Honey Mustard'),
('Veggie Tasty'),
('Veggie Clubhouse'),
('McVegan');

INSERT INTO friesAndSides_items (item_name) VALUES
('Fries'),
('Chili Cheese Tops'),
('Mini Carrots'),
('Apples');

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

INSERT INTO desserts_items (item_name) VALUES
('McFlurry Oreo'),
('McFlurry Daim'),
('Sundae Chocolate'),
('Sundae Natural'),
('Sundae Caramel'),
('Triplet Chocolate Cookie'),
('McDonut Chocolate'),
('Apple Pie');


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
