# Initializing the variables
inventory = 0

# Continuous loop
while True:
    stock = input("Enter stock quantity (or type 'quit' to exit): ")

    # Check if user wants to quit
    if stock.lower() == "quit":
        break

    # Check if input is a valid integer
    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        continue


    # Convert input to integer
    stock = int(stock)

    # Add stock to inventory
    inventory += stock