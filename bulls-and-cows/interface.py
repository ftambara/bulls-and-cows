"""
UI responsible functions.
No other module should interface with the user.
game.py objects are the intended clients.
"""

import time
from enum import Enum

"""
_MENU_OPTIONS

Quit is automatically appended.
Write in intended order of appearance.
Don't forget to reflect changes in _main_menu()
"""
_MENU_OPTIONS = [
    "Start game",
    "Settings",
    "Instructions",
    "About",
]

def start_screen():
    """
    Welcome user, launch main menu.
    """
    print("Welcome to the Bulls n' Cows game.\n\n")
    _main_menu()


def _main_menu():
    """
    Give all options to user.
    Call appropriate action.
    """

    options_dict = {opt:str(comm) for (opt, comm) 
                    in zip(_MENU_OPTIONS, range(len(_MENU_OPTIONS)))}
    options_dict["Quit"] = "q"

    commands_dict = {comm:opt for (opt, comm) in options_dict.items()}

    # Use _MENU_OPTIONS to keep intended order
    for opt in _MENU_OPTIONS + ["Quit"]:
        print(f"[{options_dict[opt]}] {opt}")
    
    while True:
        command = input()
        if command not in commands_dict:
            print("Unrecognized option. Choose one from the commands "\
                  +"in brakects.")
            continue
        else:
            break

    option = commands_dict[command]
    print("Option:", option)

    match option:
        case "Quit":
            ...
        case "Start game":
            ...
        case "Settings":
            ...
        case "Instructions":
            ...
        case "About":
            ...

def _instructions_screen():
    """Show game instructions to the user"""
    ...

def _settings_screen():
    """Allow the user to configure the game."""
    ... # Feature idea: Store last settings

def _game_mode_menu():
    ...

def _other_settings_menu():
    ...

def _about_screen():
    """Show information about the project"""

def _clear_screen():
    import os
    # for windows
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def human_take_guess(possible_digits):
    while True:
        guess = input("Write your guess:\n")
        try: 
            for d in guess:
                if d not in possible_digits:
                    raise ValueError
        except ValueError:
            print(f"Possible digits: {','.join(possible_digits)}")
            print(f"At least this digit was wrong: {d}. Try again\n")
            continue
        else:
            return list(guess)