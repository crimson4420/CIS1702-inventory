from src.storage import load_inventory, save_inventory
from src.ui import (
    print_menu,
    get_menu_choice,
    print_stock_table,
    prompt_new_item,
    prompt_update_fields,
    prompt_search_query,
    prompt_item_id,
)
from src.inventory import add_item, update_item, remove_item, search_by_name, find_by_id


def main():
    inventory = load_inventory()
    print(f"Loaded {len(inventory)} item(s).")

    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == "1":
            # Add Item
            item_id, name, price, qty = prompt_new_item()
            ok, msg = add_item(inventory, item_id, name, price, qty)
            print(msg)

        elif choice == "2":
            # View Stock
            print_stock_table(inventory)

        elif choice == "3":
            # Update Item
            item_id, new_name, new_price, new_qty = prompt_update_fields()
            ok, msg = update_item(inventory, item_id, new_name, new_price, new_qty)
            print(msg)

        elif choice == "4":
            # Search
            query = prompt_search_query()
            results = search_by_name(inventory, query)
            if results:
                print_stock_table(results)
            else:
                print("No matching items found.")

        elif choice == "5":
            # Remove Item
            item_id = prompt_item_id("enter")
            ok, msg = remove_item(inventory, item_id)
            print(msg)

        elif choice == "6":
            # Save & Exit
            if save_inventory(inventory):
                print("Inventory saved. Goodbye!")
            else:
                print("Error: Could not save inventory file.")
            break


if __name__ == "__main__":
    main()