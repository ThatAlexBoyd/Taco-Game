# Taco Maker#

This a text-based Python game developed to help learn the Python language. It is my first project in Python; and while things may not be done the most efficient way, it was a good learning experience.

## How To Play ##

The goal of the game is to BUY various ingredients and use them to CRAFT different Mexican dishes. Once CRAFTED you can take the foods to various locations to SELL. After a a day of SELLING, profits are made and a new day begins!

### BUY ###
There are a total of 7 ingredients. Each ingredients will give you a number of servings per purchase. They are as follows:

Ingredients   | Price         | Servings
------------- | ------------- | -------------
Tortilla      | $10           | 100
Meat          | $17           | 75
Sour Cream    | $20           | 25
Cheese        | $20           | 50
Beans         | $12           | 100
Hot Sauce     | $10           | 100
Vegetables    | $30           | 20

### CRAFT ####
After purchasing various items you can combine them to craft different combinations of items. All items sell for fixed amounts that cover the cost of the ingredients to make, plus earning a profit. The foods are:

Food          | Recipe
------------- | -------------
Taco          | (1) Tortilla (1) Meat (1) Cheese
Taco Supreme  | (1) Tortilla (1) Meat (1) Cheese (1) Sour Cream (1) Vegetables
Burrito       | (1) Tortilla (1) Meat (1) Cheese (1) Sour Cream (1) Hot Sauce
Bean Burrito  | (1) Tortilla (1) Bean (1) Cheese (1) Sour Cream (1) Hot Sauce
10 Layer Burrito  | (2) Tortilla (2) Meat (2) Cheese (1) Sour Cream (1) Hot Sauce (1) Bean (1) Vegetable
Pintos and Cheese     | (2) Bean (1) Sour Cream (1) Cheese
Mexican Pizza | (2) Tortilla (1) Meat (1) Cheese (1) Sour Cream (1) Hot Sauce (1) Vegetable
Nachos        | (2) Tortilla (2) Meat (2) Cheese (1) Sour Cream (2) Bean (1) Hot Sauce (1) Vegetable
Quesdilla     | (2) Tortilla (1) Meat (3) Cheese (1) Hot Sauce

### SELL ###
With your various foods crafted it is time to sell them. There are various locations in which you can go sell. Each location will have a different number of potential customers as well as customers that have preferences in foods. The different locations break down as: 

Location      | Cost          | Max Customers
------------- | ------------- | -------------
Parking Lot   | $0            | 100
Central Park  | $100          | 300
Main Street   | $150          | 500
Food Court    | $250          | 1,000
Amusement Park| $300          | 5,000
Sports Venue  | $500          | 10,000

### Last Notes ###
* The commands to type in are very literal at the moment (e.g. you need to type 'parking lot' for it to recognize)

* Typing 'info' from screens will bring up you inventory and current money

## Updates ##
* v 0.2 - Code optimization (removed ~110 lines)
