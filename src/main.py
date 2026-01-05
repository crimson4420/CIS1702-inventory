from src.validation import get_non_empty_string, get_int, get_float, get_choice


def main():
    name = get_non_empty_string("Enter a product name: ")
    qty = get_int("Enter quantity (0+): ", min_value=0)
    price = get_float("Enter price (0+): ", min_value=0)
    option = get_choice("Choose (a)dd, (v)iew, (e)xit: ", ["a", "v", "e"])

    print("\nYou entered:")
    print(name, qty, price, option)


if __name__ == "__main__":
    main()