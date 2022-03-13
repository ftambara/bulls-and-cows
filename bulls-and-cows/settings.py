"""
    - Create game configuration
    - Manipulate existing settings
    - Answer settings queries
"""
_GAME_MODES = {
    # Game_mode: (max_points, num_len, possible_digits, max_turns)
    "Pointless": (30, 5, list(range(0, 9+1))+list('ABCDEF'), 10),
    "Focused": (30, 5, list(range(0, 9+1)), 7),
    "Normal": (30, 5, list(range(0, 9+1)), 10),
    "Quick": (10, 5, list(range(1, 4+1)), 5),

}

class Settings(object):
    def __init__(self, game_mode="Normal"):
        self.set_game_mode()
    def set_game_mode(self, max_points, hid_num_length, possible_digits,
                      max_turns):
        self.max_points = max_points
        
        self.hid_num_cons = hid_num_length, list(possible_digits)
        self.hid_num_len = hid_num_length
        self.possible_digits = list(possible_digits)
        
        self.max_turns = max_turns

def set_game_mode(settings: Settings, mode: str = "Normal"):
    """
    Modes:
        - Pointless
        - Focused
        - Normal
        - Quick
    To see the differences between them, check out the README.md file at the 
    ftambara/bulls-and-cows repository.
    """
    settings.set_game_mode(*_GAME_MODES[mode])