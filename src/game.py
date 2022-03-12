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
    def take_guess(self):
        """
        Make the player take a guess.
        Return a valid guess.
        """
        raise NotImplementedError

class HumanPlayer(object):
    def take_guess(self):
        pass

class ComputerPlayer(object):
    def take_guess(self):
        pass
    """
    Plus a few private methods that call the appropiate AI functions.
    """

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

class Settings(object):
    """
    Note: Will be moved to settings.py once settings start being developed
    """
    def __init__(self, max_points, hid_num_length, possible_digits,
                 max_turns, collate=False):
        self.max_points = max_points
        self.hid_num_cons = hid_num_length, possible_digits
        self.max_turns = max_turns
        self.collate = collate

class Game(object):
    """
    Keep track of number of players. Calls each round. 
    Track score. Detects end game condition. Announces winner.
    """
    def __init__(self, players: list[Player], settings: Settings):
        self._scores = {player:0 for player in players}
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
            self._game_done = True
            keep_going = 0
            for s in self._scores:
                if s < self._settings.max_points:
                    keep_going += 1
                    if keep_going == 2:
                        # At least 2 people aren't done yet, game is not done
                        self._game_done = False
        
        return self._players

    def _play_round(self):
        """
        Make each player play turns until the round is done.
        Update players dict with obtained scores.
        """

        keep_going = [p for p,s in self._scores 
                        if s < self._settings.max_points]

        # Generate a hidden number per player
        hidden_numbers = {}
        for player in keep_going:
            hidden_numbers[player] = HiddenNumber(*self._settings.hid_num_cons)

        # TODO Code reuse, check abstraction levels
        
        # If collate is on, make each player take a turn at a time until
        # everyone's round is over
        if self._settings.collate is True:
            round_is_done = False
            turn_num = 1
            while round_is_done is False and len(keep_going) > 0:
                keep_going_this_round = keep_going[:]
                ... # TODO Visual feedback turn number
                for player in keep_going_this_round:
                    guess = player.take_guess()
                    bulls, cows = hidden_numbers[player].get_matches(guess)
                    ...    # TODO Give visual feedback: bulls, cows
                    if bulls == self._settings.hid_num_cons[0]:   # TODO legibility
                        # Hidden number discovered
                        del keep_going[player]
                        score = self._get_round_score(turn_num)
                        self._scores[player] += score
                        ...    # TODO Visual feedback: You guessed right
                        ... # TODO Visual feedback: Show score
                    elif turn_num+1 > self._settings.max_turns:
                        # Time is up
                        score = self._get_round_score(turn_num, guessed=False)
                        self._scores[player] += score
                        ...    # TODO Visual feedback: time is up                    
                        ... # TODO Visual feedback: Show score

                turn_num += 1
                if turn_num > self._settings.max_turns:
                    round_is_done = True
            return
        else:
            for player in keep_going:
                turn_num = 1
                round_is_done = False
                while round_is_done == False:
                    ... # TODO Visual feedback turn number
                    guess = player.take_guess()
                    bulls, cows = hidden_numbers[player].get_matches(guess)
                    ...    # TODO Give visual feedback: bulls, cows
                    if bulls == self._settings.hid_num_cons[0]:   # TODO legibility
                        # Hidden number discovered
                        score = self._get_round_score(turn_num)
                        ...    # TODO Visual feedback: You guessed right
                    elif turn_num+1 > self._settings.max_turns:
                        # Time is up
                        round_is_done = True
                        score = self._get_round_score(turn_num, guessed=False)
                        ...    # TODO Visual feedback: time is up
                    
                    turn_num += 1
                self._scores[player] += score
                ... # TODO Visual feedback: Show score

    def _get_round_score(self, num_turns, guessed=True):
        # TODO move it to settings/game mode object
        return ...