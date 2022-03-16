"""
    - Create game configuration
    - Manipulate existing settings
    - Answer settings queries
"""
_GAME_MODES = {
    # Game_mode: (max_points, num_len, possible_digits, max_turns)
    "Pointless": (30, 5, list('0123456789')+list('ABCDEF'), 10),
    "Focused": (30, 4, list('0123456789'), 7),
    "Normal": (4, 4, list('0123456789'), 2),
    "Quick": (10, 3, list('012345'), 5),

}

class Settings(object):
    def __init__(self):
        self.collate = False

    def set_human_players(self, num_human_players: int):
        self.num_human_players = num_human_players

    def set_computer_player(self, computer_player: bool):
        self.computer_player = computer_player

    def set_game_mode(self, mode):
        mp, num_len, digits, turns = _GAME_MODES[mode]
        self.max_points = mp
        
        self.hid_num_cons = num_len, list(digits)
        self.hid_num_len = num_len
        self.possible_digits = list(digits)
        
        self.max_turns = turns

    def _get_round_score(self, num_turns, guessed=True):
        return num_turns if guessed else int(self.max_turns*1.5)

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