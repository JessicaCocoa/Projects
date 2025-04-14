import time

class People:
    def __init__(self, name=""):
        self.name = name

    def customer_name(self):
        self.name = input("What's your name for the order? ")
        print(f"Hello, {self.name}! Menu: Please choose type of food. Wings or Fries : ")

class Menu:
    def __init__(self):
        self.foods = {"fries": 2, "wings": 20}  # Menu Dictionary

    def display_food(self):
        for item, cost in self.foods.items():
            print(f"{item}: ${cost}")

class Order(Menu):
    def __init__(self):
        self.cart = {}  # Makes person cart

    def add_food_to_cart(self):
        food = input("Which food do you want?: ").lower()
        if food in self.foods:
            quantity = int(input(f"How many {food}s would you like to buy?: "))
            self.cart[food] = self.cart.get(food, 0) + quantity
            print(f"You ordered {quantity} {food}.")


class Payment(Menu):
    def __init__(self):
        self.payment_status = False  # Track payment status

    def process_payment(self):
        payment_method = input("Which type of payment method would you like to use? (CC or Cash): ").lower()
        if payment_method =="cc" or "cash":
            self.payment_status = True
            print ("You have paid for you food!")
        else:
            print("Invalid payment method.")
            self.payment_status = False
        return self.payment_status

    def delivery_or_pickup(self):
        if self.payment_status == True:
            mode = input("Would you like to pick up or have delivery? ").lower()
            if mode == "pick up":
                print("Your order will be ready for pick-up in 20 minutes. We will text you when it's done.")
            elif mode == "delivery":
                print("Your order will be delivered to your address. We will text you when we are done makining it!")
            else:
                print("Invalid response.")
        else:
            print("You have not paid yet. Please Pay")
            self.menu.display_food()

class Kitchen:
    def kitchen_update(self):
        time.sleep(20 * 60)  # Simulates waiting time  ##was not sure how I would set this off from payment, so I did a static clock
        print("It has been 20 minutes. Food is done!")

class Inventory(Order):
    def __init__(self):
        self.master_list = []


    def check_been_ordered(self):
        print("Inventory Levels for what's been ordered:")
        self.master_list.extend(self.cart.keys())

        for item, quantity in self.master_list.items():
            print(f" You need to buy for Inventory : {item}: {quantity}")

class LoyaltyPoints:
    def __init__(self, points=0):
        self.points = points

    def add_points(self, price):
        earned_points = int(price / 10)  # Earn 1 point for every $10 spent ##giving price a variable
        self.points += earned_points ##adding points up
        print(f"You earned: {self.points} points for this delivery!")

def main():

    choice = input("Would you like to order food from the Chicken Wing Store? yes or no? : ").lower()
    while choice == "yes":
        people = People()
        people.customer_name()
        menu = Menu()
        menu.display_food()
        order = Order()
        order.add_food_to_cart()

        # Calculate total price
        total_price = sum (order.cart[food] * order.cart) #I am trying to multiply the items in my dictionary with the quantity of items I have ordered..
        payment = Payment()
        if payment.process_payment():
            loyalty = LoyaltyPoints()
            loyalty.add_points(total_price)
            kitchen = Kitchen()
            payment.delivery_or_pickup()
            inventory = Inventory()
            kitchen.kitchen_update()
            inventory.check_been_ordered()
        else:
            print("Payment not completed. Please try again.")

        choice = input("Would you like to order more? yes or no? : ").lower()
    else:
        print("Thank you!!")

if __name__ == "__main__":
    main()






























