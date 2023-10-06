from datetime import datetime
Name=input("Enter customer name:")
itmes = {
    'Rice': 20, 'Sugar': 25, 'Oil': 90, 'Soap': 10, 'Boost': 10, 'Dairymilk': 10, 'Salt': 40, 'Perfume': 190,
    'Milk powder': 200, 'Biscuit': 20, 'shampoo': 30, 'chips': 20, 'popcorn': 23, 'Bread': 20, 'Colagate': 20
}

item_list = '''
Rice          Rs 20/kg
Sugar         Rs 25/kg
Oil           Rs 90/liter
Soap          Rs 10/pec
Boost         Rs 10/pec
Dairymilk     Rs 10/pec
Salt          Rs 40/kg
Perfume       Rs 190/each
Milk powder   Rs 200/kg
Biscuit       Rs 20/each
shampoo       Rs 30/each
chips         Rs 20/each
popcorn       Rs 23/each
Bread         Rs 20/each
Colagate      Rs 20/each
'''

pricelist = []
totalprice = 0

while True:
    print(item_list)
    user_choice = int(input("Enter 1 to buy an item or 2 to exit: "))
    
    if user_choice == 2:
        break
    elif user_choice == 1:
        item = input("Enter the item: ")
        quantity = int(input("Enter quantity: "))
        
        if item in itmes:
            price = quantity * itmes[item]
            pricelist.append((item, quantity, price, price))
            totalprice += price
        else:
            print("Sorry, the entered item is not available.")
    else:
        print("Invalid input. Please enter 1 or 2.")


gst = (totalprice * 5) / 100
final_amount = totalprice + gst

print("\n******** Invoice ********")
print(f"Customer Name: {Name}")
print("-------------------------------")
for item, quantity, price, _ in pricelist:
    print(f"{item} x {quantity}: Rs {price}")
print("-------------------------------")
print(f"Total Price: Rs {totalprice}")
print(f"GST (5%): Rs {gst}")
print(f"Final Amount: Rs {final_amount}")
print("Thanks for purchasing-welcome again")