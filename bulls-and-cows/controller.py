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

settings = st.Settings()
# Who should handle the players initialization and action execution?
game = logic.Logic()

def _initiate_game():
    game.start_game()