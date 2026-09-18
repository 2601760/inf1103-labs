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


def main():
    inventory = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            continue

        print("Valid quantity:", result)


if __name__ == "__main__":
    main()