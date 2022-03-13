"""
UI responsible functions.
No other module should interface with the user.
game.py objects are the intended clients.
"""

def start_screen():
    """
    Welcome user, launch main menu.
    """
    print("Welcome to the Bulls n' Cows game.\n")

def _main_menu():
    """
    Give all options to user.
    Call appropriate action.
    """


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