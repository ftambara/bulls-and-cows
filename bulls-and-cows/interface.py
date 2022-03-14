"""
UI responsible functions.
No other module should interface with the user.
game.py objects are the intended clients.
"""

import controller
import player
import time

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

_WAIT_BETWEEN_SCREENS = 1    # in seconds

def start_screen():
    """
    Welcome user, launch main menu.
    """
    _clear_screen()
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
        command = input("\n[_]\b\b")
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
            _clear_screen()
            controller.initiate_game()
            _end_game_screen()
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

def _clear_screen(wait=True):
    import os
    
    if wait:
        time.sleep(_WAIT_BETWEEN_SCREENS)

    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def _end_game_screen():
    ...    # Announce winner, show leaderboard
    ...    # Call function from control.py to store leaderboard


def human_take_guess(num_len, possible_digits):
    while True:
        guess = input("Write your guess:\n")
        if len(guess) != num_len:
            print(f"Your guess should be {num_len} digits long.\n")
            continue

        if len(guess) != len(set(guess)):
            print(f"All digits should be unique.\n")
            continue

        try: 
            for d in guess:
                if d not in possible_digits:
                    raise ValueError
        except ValueError:
            print(f"Possible digits: {', '.join(possible_digits)}")
            print(f"At least this digit was wrong: '{d}'. Try again.\n")
            continue
        else:
            return list(guess)

def guess_result(bulls, cows):
    print(f"B:{bulls}   C:{cows}\n\n")

def show_active_player(player_: player.Player):
    print(player_)

def show_partial_end_round_data(score, hidden_num, guessed):
    if not guessed:
        print(f"You didn't make it. The number was {hidden_num}.")
    else:
        print(f"You guessed!")

    print(f"Your round score was {score}.")
    _clear_screen()

def show_final_end_round_data(scores: dict, max_score: int):
    print("End of the round!")
    _clear_screen()
    print("Scores:\n")
    for p,s in scores.items():
        if s < max_score:
            print(f"\n{p}: {s}.")
        else:
            print(f"\n{p}: {s}. OUT!")

def show_turn(turn_num):
    print(f"Turn {turn_num}")