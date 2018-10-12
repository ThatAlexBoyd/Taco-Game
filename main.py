####################################
# File name: Main                  #
# Author: Alex Boyd                #
####################################

import random
import time
import sys

# CLASSES ##############################################


class Ingredient:
    def __init__(self, _name, _cost, _servings):
        self.name = _name
        self.cost = _cost
        self.servings = _servings


class Food:
    def __init__(self, _name, _value, _recipe):
        self.name = _name
        self.value = _value
        self.recipe = _recipe


class Location:
    def __init__(self, _name, _cost, _pref, _customer_min, _customer_max):
        self.name = _name
        self.cost = _cost
        self.pref = _pref
        self.customer_min = _customer_min
        self.customer_max = _customer_max

    def get_customers(self):
        temp_customers = []
        num_customers = random.randint(self.customer_min, self.customer_max)
        temp_foods = self.get_foods(num_customers)
        random.shuffle(temp_foods)
        for i in range(num_customers):
            temp_pref1 = temp_foods[len(temp_foods) - 1]
            temp_foods.pop()
            temp_pref2 = temp_foods[len(temp_foods) - 1]
            temp_foods.pop()
            temp_customers.append(Customer(temp_pref1, temp_pref2))
        return temp_customers

    def get_foods(self, customer_amount):
        temp_foods = []
        for i in range(customer_amount * 2):
            rand_num = random.randint(0, 100)
            if rand_num <= 30:
                temp_foods.append(self.pref[0])
            elif rand_num <= 60:
                temp_foods.append(self.pref[1])
            else:
                temp_foods.append(random.choice(foods))
        return temp_foods


class Customer:
    def __init__(self, _pref1, _pref2):
        self.pref1 = _pref1
        self.pref2 = _pref2
#######################################################

# VARS #################################################
money = 50

# Ingredients ########

tortilla = Ingredient('tortilla', 10, 100)
meat = Ingredient('meat', 17, 75)
cream = Ingredient('sour cream', 20, 25)
cheese = Ingredient('cheese', 20, 50)
bean = Ingredient('beans', 12, 100)
sauce = Ingredient('hot sauce', 10, 100)
veg = Ingredient('vegetables', 30, 20)

ingredients = [tortilla, meat, cream, cheese, bean, sauce, veg]

inventory_ingredients = {tortilla: 0, meat: 0, cream: 0, cheese: 0, bean: 0, sauce: 0, veg: 0}

# Foods #######

taco = Food('taco', 2, {tortilla: 1, meat: 1, cheese: 1})
taco_supreme = Food('taco supreme', 4, {tortilla: 1, meat: 1, cream: 1, cheese: 1, veg: 1})
burrito = Food('burrito', 3, {tortilla: 1, meat: 1, cream: 1, cheese: 1, sauce: 1})
burrito_layer = Food('layered burrito', 5, {tortilla: 2, meat: 2, cream: 1, cheese: 2, bean: 1, sauce: 1, veg: 1})
burrito_bean = Food('bean burrito', 3, {tortilla: 1, cream: 1, cheese: 1, bean: 1, sauce: 1})
pintos_cheese = Food('pintos and cheese', 2, {cream: 1, cheese: 1, bean: 2})
mexican_pizza = Food('mexican pizza', 5, {tortilla: 2, meat: 1, cream: 1, cheese: 1, sauce: 1, veg: 1})
nachos = Food('nachos', 6, {tortilla: 2, meat: 2, cream: 1, cheese: 2, bean: 2, sauce: 1, veg: 1})
quesdilla = Food('quesdilla', 3, {tortilla: 2, meat: 1, cheese: 3, sauce: 1})

foods = [taco, taco_supreme, burrito, burrito_bean, burrito_layer, pintos_cheese, mexican_pizza, nachos, quesdilla]

inventory_foods = {taco: 0, taco_supreme: 0, burrito: 0, burrito_bean: 0, burrito_layer: 0, pintos_cheese: 0,
                   mexican_pizza: 0, nachos: 0, quesdilla: 0}

# Locations
parking_lot = Location('parking lot', 0, [taco, burrito], 60, 100)
central_park = Location('central park', 100, [quesdilla, pintos_cheese], 150, 300)
main_street = Location("main street", 150, [taco_supreme, burrito], 250, 400)
food_court = Location('food court', 250, [nachos, burrito_bean], 700, 1000)
amusement_park = Location('amusement park', 300, [burrito_bean, mexican_pizza], 4000, 5000)
sport_venue = Location('sports venue', 500, [nachos, burrito_layer], 7500, 10000)

locations = [parking_lot, central_park, main_street, food_court, amusement_park, sport_venue]

#######################################################


def buying_ingredient(current_ingredient):
    while True:
        global inventory_ingredients
        global money
        print("\n----" + current_ingredient.name.title() + "-----")
        print("Price: $" + str(current_ingredient.cost))
        print("Servings: " + str(current_ingredient.servings))
        response = input('\nYou have ${}, make purchase? YES or NO: '.format(money)).lower()
        if response == 'yes':
            if current_ingredient.cost <= money:
                inventory_ingredients[current_ingredient] += current_ingredient.servings
                money -= current_ingredient.cost
                print('\nPurchased: ' + current_ingredient.name.title())
                print('Money Remaining: $' + str(money))
                buy()
                return
            else:
                print('\nYou do not have enough money!')
                buy()
                return
        elif response == 'no':
            buy()
            return
        else:
            print('That is not a correct response.\n')


def crafting_food(current_food):
    while True:
        recipe = ''
        # gather the ingredients that are needed to make the passed _food
        for key, value in current_food.recipe.items():
            recipe += key.name + ": " + str(value) + "\n"
        print('\n----' + current_food.name.upper() + ' RECIPE----\n{}'.format(recipe))
        response = input("Enter the NUMBER of {}'S to make or CANCEL: ".format(current_food.name.upper()))
        try:
            crafting_amount = int(response)
            if crafting_check(current_food, crafting_amount):
                crafting_inventory(current_food, crafting_amount)
                return
            else:
                print('\nYou do not have enough ingredients for that!')
                craft()
                return
        except ValueError:
            if response == 'cancel':
                craft()
                return
            elif response == 'info':
                display_inventory()
            else:
                print('That is not a number')


def crafting_check(current_food, crafting_amount):  # checks to see if the player has enough ingredients to make food
    for key, value in current_food.recipe.items():
        if inventory_ingredients.get(key) < (current_food.recipe.get(key) * crafting_amount):
            return False
    return True


def crafting_inventory(current_food, crafting_amount):
    # Remove ingredients from inventory
    for key, value in current_food.recipe.items():
        inventory_ingredients[key] = (inventory_ingredients[key] - crafting_amount)
    # Add crafted food to food inventory
    inventory_foods[current_food] += crafting_amount
    print('\nCrafted: {0} {1}(s)'.format(str(crafting_amount), str(current_food.name)))
    craft()
    return


def selling_location(current_location):
    while True:
        print("\n----{}-----".format(current_location.name.title()))
        print('Cost: ${}'.format(str(current_location.cost)))
        print('Max Customers: {}'.format(str(current_location.customer_max)))
        response = input('\nDo you want travel to the location? YES or NO: ')
        if response == 'yes':
            if current_location.cost <= money:
                simulate_day(current_location)
                return
            else:
                print('You do not have enough money!')
                sell()
                return
        elif response == 'no':
            sell()
            return
        else:
            print("{} is not a location.\n".format(response.upper()))
            selling_location(current_location)


def simulate_day(current_location):
    global money
    global inventory_foods
    customers = current_location.get_customers()
    counter_served = 0
    counter_customer = 0
    counter_money = 0
    while counter_customer < len(customers):
        rand_num = random.randint(0, 100)
        if inventory_foods[customers[counter_customer].pref1] > 0:
            inventory_foods[customers[counter_customer].pref1] -= 1
            counter_money += customers[counter_customer].pref1.value
            counter_served += 1
        elif rand_num <= 50:
            if inventory_foods[customers[counter_customer].pref2] > 0:
                inventory_foods[customers[counter_customer].pref2] -= 1
                counter_money += customers[counter_customer].pref2.value
                counter_served += 1
        elif rand_num >= 75:
            settling_foods = [random.choice(list(inventory_foods.keys())), random.choice(list(inventory_foods.keys()))]
            counter_settling = 0
            for _food in settling_foods:
                if inventory_foods[settling_foods[counter_settling]] > 0:
                    inventory_foods[_food] -= 1
                    counter_money += settling_foods[counter_settling].value
                    counter_served += 1
                    break
                counter_settling += 1
        counter_customer += 1
    money += counter_money
    end_of_day(counter_served, counter_money)
    return


def end_of_day(customers_served, money_made):
    print("\n----END OF DAY REPORT----")
    print('Customers: {}'.format(str(customers_served)))
    print("Money Made: ${}".format(str(money_made)))
    thrown_out_food = ''
    for f in inventory_foods:
        if inventory_foods[f] != 0:
            thrown_out_food += f.name.title() + "s(" + str(inventory_foods[f]) + "), "
        inventory_foods[f] = 0
    print('Thrown Out: ' + thrown_out_food)
    input("\nPress ANY key to continue.")
    main_menu()
    return


def display_inventory():
    current_ingredients = ''
    current_foods = ''
    # grabs all ingredients and their values to display
    for _ingredients in inventory_ingredients:
        current_ingredients += _ingredients.name.title() + ": " + str(inventory_ingredients[_ingredients]) + "\n"
    print('\n----INGREDIENTS---- \n' + current_ingredients)
    for _food in inventory_foods:
        current_foods += _food.name.title() + ": " + str(inventory_foods[_food]) + "\n"
    print('\n----FOODS----\n' + current_foods)
    print("MONEY: $" + str(money))
    return


def main_menu():
    while True:
        print('\nMain Menu: you can BUY, CRAFT, or SELL.')
        response = input('What would you like to do: ').lower()
        choices = {'buy': buy, 'craft': craft, 'sell': sell}
        if response in choices:
            choices[response]()
            return
        elif response == 'info':
            display_inventory()
        else:
            print('\n{} is not an option.'.format(response.upper()))


def buy():
    while True:
        print("\nIngredients available to buy: {}.".format(', '.join(i.name for i in ingredients)))
        response = input('Choose an item or CANCEL: ').lower()
        choices = {'tortilla': tortilla, 'meat': meat, 'sour cream': cream, 'cheese': cheese, 'beans': bean,
                   'hot sauce': sauce, 'vegetables': veg}
        if response in choices:
            buying_ingredient(choices[response])
            return
        elif response == 'cancel':
            main_menu()
            return
        elif response == 'info':
            display_inventory()
        else:
            print('\n{} is not an ingredient.'.format(response.upper()))


def craft():
    while True:
        print("\nFoods available to craft: {}.".format(', '.join(i.name for i in foods)))
        response = input('Choose an item or CANCEL: ').lower()
        choices = {'taco': taco, 'taco supreme': taco_supreme, 'burrito': burrito, "layered burrito": burrito_layer,
                   'bean burrito': burrito_bean, 'pintos and cheese': pintos_cheese, 'mexican pizza': mexican_pizza,
                   'quesdilla': quesdilla}
        if response in choices:
            crafting_food(choices[response])
            return
        elif response == 'cancel':
            main_menu()
            return
        elif response == 'info':
            display_inventory()
        else:
            print('\n{} is not a food'.format(response.upper()))


def sell():
    while True:
        print('\nLocations available to sell at: {}.'.format(', '.join(i.name for i in locations)))
        response = input('Choose a location or CANCEL: ').lower()
        choices = {'parking lot': parking_lot, 'central park': central_park, 'food court': food_court,
                   'amusement park': amusement_park, 'sports venue': sport_venue}
        if response in choices:
            selling_location(choices[response])
            return
        elif response == 'cancel':
            main_menu()
            return
        elif response == 'info':
            display_inventory()
        else:
            print('\n{} is not a location'.format(response.upper()))

main_menu()
