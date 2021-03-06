"""
Module responsible for the lower level game control functionality:
    - Starting the game
    - Creating and updating the leaderboard file
    - Creating and updating the settings file
    - Terminating the game

interface.py functions are the intended clients.
"""

import logic
import settings as st
import player

_settings = st.Settings()

def _gen_player_list():
    return [player.HumanPlayer() for _ in range(_settings.num_human_players)]\
        +([player.ComputerPlayer()] if _settings.computer_player else [])


def update_game_mode(game_mode):
    _settings.set_game_mode(game_mode)

def update_human_players(num):
    _settings.set_human_players(num)

def update_computer_player(bool_):
    _settings.set_computer_player(bool_)

def _load_default_settings():
    update_game_mode("Normal")
    update_human_players(2)
    update_computer_player(False)


_load_default_settings()
_players = _gen_player_list()

def initiate_game():
    _game = logic.Logic(_players, _settings)
    _game.start_game()
    return _game.get_scores()