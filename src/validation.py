#provides reusable input validation functions
#to ensure the program never crashes due to invalid user input

from typing import Iterable, Optional


def get_non_empty_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: input cannot be empty. Please try again.")


def get_int(prompt: str, min_value: Optional[int] = None, max_value: Optional[int] = None) -> int:
    #repeatedly prompts the user to input a valid integer 
    #for some features a miniumum value is also enforced
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Error: please enter a whole number.")
            continue

        if min_value is not None and value < min_value:
            print(f"Error: value must be at least {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Error: value must be at most {max_value}.")
            continue

        return value


def get_float(prompt: str, min_value: Optional[float] = None, max_value: Optional[float] = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Error: please enter a number.")
            continue

        if min_value is not None and value < min_value:
            print(f"Error: value must be at least {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Error: value must be at most {max_value}.")
            continue

        return value


def get_choice(prompt: str, choices: Iterable[str]) -> str:
    choices_list = list(choices)
    choices_lower = {c.lower(): c for c in choices_list}

    while True:
        raw = input(prompt).strip().lower()
        if raw in choices_lower:
            return choices_lower[raw]
        print(f"Error: please choose one of: {', '.join(choices_list)}")