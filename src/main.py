from src.inventory import add_item, update_item, remove_item, search_by_name


def main():
    inv = []

    ok, msg = add_item(inv, "A001", "Milk", 1.25, 10)
    print(ok, msg)

    ok, msg = add_item(inv, "A001", "Duplicate Milk", 1.50, 2)
    print(ok, msg)

    ok, msg = update_item(inv, "A001", new_price=1.35, new_quantity=8)
    print(ok, msg)

    results = search_by_name(inv, "mi")
    print("Search results:", results)

    ok, msg = remove_item(inv, "A001")
    print(ok, msg)

    ok, msg = remove_item(inv, "A001")
    print(ok, msg)


if __name__ == "__main__":
    main()