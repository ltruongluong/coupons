from inventory import *
from cart import *
from coupons import *

def display_items(items):
    print("Inventory:")
    for item in items:
        print(f"{item.name} (${item.price})")

def display_coupons(coupons):
    print("Coupons:")
    for coupon in coupons:
        print(f"Code: {coupon.code} (for {int(coupon.percentage * 100)}% OFF!)")
        
#items 
milk = Inventory("milk", 4)
beans = Inventory("beans", 2)
candy = Inventory("candy", 1)
items = [milk, beans, candy]

#coupons
half = Coupons("half", .5)
ten = Coupons("ten", .1)
coupons = [half, ten]

#cart
cart = Cart()


print("Welcome to the Store!")
print("""What would you like to do?
1: View Inventory
2: View Coupons 
3: View Cart
4: Add to Cart
5: Checkout """)
option = input("Type 1-5: ")

if option == '1':
    display_items(items)
elif option == '2':
    display_coupons(coupons)
elif option == '3':
    print(cart.items)
elif option == '4':
    print("which item would you like to add to cart:")
    for item in items:
        print(item.name)