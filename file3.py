import math  # Import the math module for mathematical operations (though not used here)

# List indicating if shopping is available
isshopping = ['yes', 'no']

# List of products with their names and prices
products = [
    {"name": "orange", "price": 200},
    {"name": "banana", "price": 100},
    {"name": "mango", "price": 50},
    {"name": "eggs", "price": 75}
]

# Initialize total cost
total_bill = 0

while True:
    # Prompt the user to see if they want to shop
    print(f"Do you want to shop? : {isshopping}")
    yesORno = input("Enter 'yes' or 'no': ").lower()  # Convert input to lowercase for case insensitivity

    if yesORno == isshopping[0]:
        # Display available products
        print(f"Make your choice from: {[product['name'] for product in products]}")

        choice = input("Enter the product name: ").lower()  # Convert input to lowercase

        # Find the product with the given name
        selected_product = next((product for product in products if product['name'] == choice), None)

        if selected_product:
            quantity = int(input(f"Enter the quantity of {choice}: "))

            # Calculate total cost
            price_per_unit = selected_product['price']
            total_cost = price_per_unit * quantity
            total_bill += total_cost

            print(f"You chose {quantity} {choice}(s). Your total cost for this item is ${total_cost}.")
        else:
            print("Invalid product choice.")
    elif yesORno == isshopping[1]:
        print(f"Thank you for shopping. Your total bill is ${total_bill}. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
