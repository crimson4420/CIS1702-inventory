# CIS1702-inventory
Load inventory from file on startup

Menu: Add / View / Update / Search / Remove / Save & Exit

Items have unique ID, name, price, quantity

Formatted table output

Data persists between sessions

Graceful error handling (invalid input, item not found)

Agree team roles + commit evidence strategy
Charlie Connor:storage + validation + add/update/remove core
Kenzie Anderton:UI/table + search + testing lead + report skeleton

inventory is a list of the items used for the code
example item: {"id":"A001","name":"Milk","price":1.25,"quantity":10}

storage layer: safe failure for missing files,empty files, bad json files and writes json with indent
