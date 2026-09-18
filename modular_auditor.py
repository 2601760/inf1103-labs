def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit' to exit): ")

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        print("Error: Please enter a valid integer.")
        return None

    quantity = int(user_input)

    if quantity < 0:
        print("Error: Negative values are not allowed.")
        return None

    return quantity


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def main():
    inventory = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            continue

        tax = calculate_tax(result)
        inventory = process_delivery(inventory, result)

        print(f"Delivery: {result} units | Tax: ${tax:.2f}")
        print("Current Inventory:", inventory)


if __name__ == "__main__":
    main()