#!/usr/bin/env python3
"""
This module contains the main game logic
"""

class Player(object):
    """
    Abstract class. Instance subclasses HumanPlayer or ComputerPlayer instead.
    """
    def __init__(self, number):
        pass
    def play_turn(self):
        raise NotImplementedError

class HumanPlayer(object):
    def play_turn(self):
        pass

class ComputerPlayer(object):
    def play_turn(self):
        pass
    """
    Plus a few private methods that call the appropiate AI functions.
    """

class Settings(object):
    """
    Note: Will be moved to settings.py once settings start being developed
    """
    def __init__(self, max_points, hid_num_length, possible_digits,
                 max_turns, collate=False):
        self.max_points = max_points
        self.hid_num_length = hid_num_length
        self.possible_digits = possible_digits
        self.collate = max_turns

class Game(object):
    """
    Keep track of number of players. Calls each round. 
    Track score. Detects end game condition. Announces winner.
    """
    def __init__(self, players: list[Player], settings: Settings):
        self._players = {player:0 for player in players}
        self._settings = settings
        self._game_done = False
        pass
        
    def start_game(self):
        """
        Execute a full game.
        Return dict of players and their final scores.
        """
        while self._game_done is False:
            self._play_round()
        
        return self._players

    def _play_round(self):
        """
        Make each player play turns until the round is done.
        Update players dict with obtained scores.
        """

        keep_going = [p for p,s in self._players 
                        if s < self._settings.max_points]

        if self._settings.collate is True:
            for player in keep_going:
                ...

    def _play_turn(self, player: Player):
        """
        Make the player play a single turn.
        Return a tuple (num_bulls, num_cows).
        """
        pass


class HiddenNumber(object):
    def __init__(self, num_digits: int, possible_digits):
        """
        Generate a random number according to the given constraints.
        num_digits: length of the hidden number.
        possible_digits: an iterable object.
        """
        list.append()
        pass
    def get_matches(self, number):
        """
        Return a tuple (number of bulls, number of cows)
        """
        pass
