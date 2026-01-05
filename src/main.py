from storage import load_inventory, save_inventory


def main():
    inv = load_inventory()
    print("Loaded items:", len(inv))

    # quick test: save a dummy item if inventory is empty
    if len(inv) == 0:
        inv.append({"id": "A001", "name": "Milk", "price": 1.25, "quantity": 10})
        ok = save_inventory(inv)
        print("Saved dummy item:", ok)


if __name__ == "__main__":
    main()