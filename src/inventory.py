from typing import List, Dict, Any, Optional, Tuple

Item = Dict[str, Any]


def _clean_id(item_id: str) -> str:
    return str(item_id).strip()


def _clean_name(name: str) -> str:
    return str(name).strip()


def find_by_id(inventory: List[Item], item_id: str) -> Optional[Item]:
    #returns the matching item dict if found , else none
    target = _clean_id(item_id)
    for item in inventory:
        if _clean_id(item.get("id", "")) == target:
            return item
    return None


def add_item(inventory: List[Item], item_id: str, name: str, price: float, quantity: int) -> Tuple[bool, str]:
    #used to add a new item with a unique id, has to be inputted with valid format
    item_id = _clean_id(item_id)
    name = _clean_name(name)

    if not item_id:
        return False, "Item ID cannot be empty."
    if not name:
        return False, "Item name cannot be empty."
    if price < 0:
        return False, "Price cannot be negative."
    if quantity < 0:
        return False, "Quantity cannot be negative."

    if find_by_id(inventory, item_id) is not None:
        return False, f"Item with ID '{item_id}' already exists."

    inventory.append(
        {"id": item_id, "name": name, "price": float(price), "quantity": int(quantity)}
    )
    return True, f"Added item '{name}' (ID: {item_id})."


def update_item(
    inventory: List[Item],
    item_id: str,
    new_name: Optional[str] = None,
    new_price: Optional[float] = None,
    new_quantity: Optional[int] = None,
) -> Tuple[bool, str]:
    #used to update an existing items name, price, and quantity or leave the quantity as it is
    item_id = _clean_id(item_id)
    item = find_by_id(inventory, item_id)
    if item is None:
        return False, f"No item found with ID '{item_id}'."

    if new_name is not None:
        new_name = _clean_name(new_name)
        if not new_name:
            return False, "New name cannot be empty."
        item["name"] = new_name

    if new_price is not None:
        if new_price < 0:
            return False, "New price cannot be negative."
        item["price"] = float(new_price)

    if new_quantity is not None:
        if new_quantity < 0:
            return False, "New quantity cannot be negative."
        item["quantity"] = int(new_quantity)
    
    if new_name is None and new_price is None and new_quantity is None:
        return False, "No changes selected."

    return True, f"Updated item (ID: {item_id})."


def remove_item(inventory: List[Item], item_id: str) -> Tuple[bool, str]:
    #used to remove an item using its ID
    item_id = _clean_id(item_id)
    item = find_by_id(inventory, item_id)
    if item is None:
        return False, f"No item found with ID '{item_id}'."

    inventory.remove(item)
    return True, f"Removed item (ID: {item_id})."


def search_by_name(inventory: List[Item], query: str) -> List[Item]:
    #used to return all items that names contain the query "case-insentitive"
    q = _clean_name(query).lower()
    if not q:
        return []
    return [item for item in inventory if q in _clean_name(item.get("name", "")).lower()]