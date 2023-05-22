class Inventory():
    def __init__(self, name, price): 
        self.name = name 
        self.price = price 

class Coupons():
    def __init__(self, code, percentage):
        self.code = code
        self.percentage = percentage


class Cart():
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    

    def add_to_cart(self):
        item_name = input("which item from the inventory would you like to add to cart:")
        for item in inventory:
            if item_name == item.name:
                self.add_item(item)
                print(f"{item.name} is added to your cart!")
                main()
    
    def display_cart(self):
        print("Inside your cart:")
        for item in self.items:
            print(f"{item.name} (${item.price})")
        main()



def display_items(inventory):
    print("Inventory:")
    for item in inventory:
        print(f"{item.name} (${item.price})")
    main()

def display_coupons(coupons):
    print("Coupons:")
    for coupon in coupons:
        print(f"Code: {coupon.code} (for {int(coupon.percentage * 100)}% OFF!)")
    main()

def check_out(cart, coupons):
    total = []
    for item in cart.items:
        total.append(item.price)
    print("Your total:", sum(total), "dollars")
    
    total_price = sum(total)
    coupon_code = input("please enter coupon code: ")
    for coupon in coupons:
        if coupon_code == coupon.code:
            total_price -= total_price * (coupon.percentage)
            print("Your new total is", total_price, "dollars")



#items 
milk = Inventory("milk", 4)
beans = Inventory("beans", 2)
candy = Inventory("candy", 1)
inventory = [milk, beans, candy]

#coupons
half = Coupons("half", .5)
ten = Coupons("ten", .1)
coupons = [half, ten]

#cart
cart = Cart()


            
def main():
    print("Main Menu:")
    print("""What would you like to do?
    1: View Inventory
    2: View Coupons 
    3: View Cart
    4: Add to Cart
    5: Checkout """)
    option = input("Type 1-5: ")

    if option == '1':
        display_items(inventory)
    elif option == '2':
        display_coupons(coupons)
    elif option == '3':
        Cart.display_cart(cart)
    elif option == '4':
       Cart.add_to_cart(cart)
    elif option == '5':
        check_out(cart, coupons)



main()