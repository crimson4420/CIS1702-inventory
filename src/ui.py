from typing import List, Dict, Any, Optional, Tuple

from src.validation import get_non_empty_string, get_int, get_float, get_choice

Item = Dict[str, Any]


def print_menu() -> None:
    print("\n=== Inventory Management System ===")
    print("1) Add Item")
    print("2) View Stock")
    print("3) Update Item")
    print("4) Search Item")
    print("5) Remove Item")
    print("6) Save & Exit")


def get_menu_choice() -> str:
    # Use get_choice so only valid options are accepted
    return get_choice("Choose an option (1-6): ", ["1", "2", "3", "4", "5", "6"])


def print_stock_table(inventory: List[Item]) -> None:
    if not inventory:
        print("\n(No items in inventory)")
        return

    # Column widths
    id_w = 10
    name_w = 25
    price_w = 10
    qty_w = 10

    print("\n" + "-" * (id_w + name_w + price_w + qty_w + 13))
    print(f"| {'ID':<{id_w}} | {'Name':<{name_w}} | {'Price':>{price_w}} | {'Qty':>{qty_w}} |")
    print("-" * (id_w + name_w + price_w + qty_w + 13))

    for item in inventory:
        item_id = str(item.get("id", ""))
        name = str(item.get("name", ""))
        price = float(item.get("price", 0.0))
        qty = int(item.get("quantity", 0))

        # price formatted to 2 decimals
        print(f"| {item_id:<{id_w}} | {name:<{name_w}} | {price:>{price_w}.2f} | {qty:>{qty_w}} |")

    print("-" * (id_w + name_w + price_w + qty_w + 13))


def prompt_new_item() -> Tuple[str, str, float, int]:
    print("\n--- Add New Item ---")
    item_id = get_non_empty_string("Enter unique item ID: ")
    name = get_non_empty_string("Enter item name: ")
    price = get_float("Enter price (0+): ", min_value=0)
    qty = get_int("Enter quantity (0+): ", min_value=0)
    return item_id, name, price, qty


def prompt_item_id(action: str = "enter") -> str:
    return get_non_empty_string(f"Please {action} the item ID: ")


def prompt_search_query() -> str:
    return get_non_empty_string("Enter name to search for: ")


def prompt_update_fields() -> Tuple[str, Optional[str], Optional[float], Optional[int]]:
    #ask user which item to update and which fields are to change
    print("\n--- Update Item ---")
    item_id = get_non_empty_string("Enter the item ID to update: ")

    print("What would you like to update?")
    print("1) Name")
    print("2) Price")
    print("3) Quantity")
    print("4) Name + Price")
    print("5) Name + Quantity")
    print("6) Price + Quantity")
    print("7) Name + Price + Quantity")

    choice = get_choice("Choose (1-7): ", ["1", "2", "3", "4", "5", "6", "7"])

    new_name: Optional[str] = None
    new_price: Optional[float] = None
    new_qty: Optional[int] = None

    if choice in ["1", "4", "5", "7"]:
        new_name = get_non_empty_string("Enter new name: ")
    if choice in ["2", "4", "6", "7"]:
        new_price = get_float("Enter new price (0+): ", min_value=0)
    if choice in ["3", "5", "6", "7"]:
        new_qty = get_int("Enter new quantity (0+): ", min_value=0)

    return item_id, new_name, new_price, new_qty