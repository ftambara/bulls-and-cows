"""
UI responsible functions.
No other module should interface with the user.
game.py objects are the intended clients.
"""

import controller
import player
import time
import settings

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
    _clear_screen(wait=0)
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

    while True:
        # Use _MENU_OPTIONS to keep intended order
        print("\n")
        for opt in _MENU_OPTIONS + ["Quit"]:
            print(f"[{options_dict[opt]}] {opt}")
        
        while True:
            command = input("\n[_]\b\b")
            if command not in commands_dict:
                print("Unrecognized option. Choose one of the commands "\
                    +"in brackets.")
                continue
            else:
                break

        option = commands_dict[command]
        print("Option:", option)

        match option:
            case "Quit":
                _quit_screen()
                _clear_screen()
                break
            case "Start game":
                _clear_screen()
                scores = controller.initiate_game()
                _clear_screen()
                _end_game_screen(scores)
            case "Settings":
                _clear_screen()
                _settings_screen()
            case "Instructions":
                _clear_screen()
                _instructions_screen()
            case "About":
                _clear_screen()
                _about_screen()

def _instructions_screen():
    """Show game instructions to the user"""

    print("- The game can be player against the machine, or by any number of "\
         +"human players plus one optional computer player.")
    print("- In the first turn of every round, the machine generates a "\
         +"hidden number for each player. The player tries to guess it. Once "\
         +"the guess is sent, the machine returns the number of bulls "\
         +"(digits present in the hidden number in the exact same position) "\
         +"and the number of cows (digits present in the hidden number in a "\
         +"different position).")
    print("- The players keeps taking turns until they either discover their "\
         +"number or exhaust the number of turns for that round (10 turns in "\
         +"most game modes)")
    print("\n")

def _settings_screen():
    """Allow the user to configure the game."""
    
    print("Customization coming soon.\n"
         +"Only default settings available for now.")
    print("That means 2 players and normal difficulty.")

def _game_mode_menu():
    ...

def _other_settings_menu():
    ...

def _about_screen():
    """Show information about the project"""
    print("I made this project with the intention of practicing some "\
         +"programming concepts- basic OOP and dealing with project size."\
         +"deal with project size.\n"
         +"My two main takeways are:\n"\
         +"   - Do less things at a time, keep feature adding under control.\n"\
         +"   - Try hard to get the object interaction right. Having a clear "\
         +"idea of how the objects should interact and who is responsible of "\
         +"what makes all the difference")

def _quit_screen():
    print("\nGoodbye!")

def _clear_screen(wait=1):
    import os
    
    time.sleep(wait)

    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def _end_game_screen(scores):
    p, s = scores[0]
    print(f"WINNER: {p} with {s} points.")
    for p, s in scores[1:]:
        print(f"{p} score: {s}")
    
    print("\nWell played!")
    

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

def show_partial_end_round_data(score, guessed, hidden_num=None):
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