#!/usr/bin/env python3
"""
This module contains the main game logic
"""

import random

import interface
import settings as st
import player

class HiddenNumber(object):
    def __init__(self, num_digits: int, possible_digits):
        """
        Generate a random number according to the given constraints.
        num_digits: length of the hidden number.
        possible_digits: list of all possible digits that the hidden number
        can be made of
        """        
        if len(possible_digits) < num_digits:
            raise ValueError("Couldn't build the hidden number."\
                             +"Too few possible digits given.")

        # Used [:] instead of list.copy() because possible digits
        self._hidden_number = random.sample(possible_digits, num_digits)

    def get_matches(self, guess: list):
        """
        Assumes guess is valid
        Return a tuple (number of bulls, number of cows)
        """
        bulls, cows = 0, 0
        for digit in guess:
            if digit in self._hidden_number:
                if guess.index(digit) == self._hidden_number.index(digit):
                    bulls += 1
                else:
                    cows += 1
        return bulls, cows

    def reveal(self):
        return self._hidden_number

def is_guess_valid(settings: st.Settings, guess: list):
    
    num_digits = settings.hid_num_cons[0]
    possible_digits = settings.hid_num_cons[1]
    
    if len(guess) != num_digits:
        return False
    
    for digit in guess:
        if digit not in possible_digits:
            return False
    
    return True

class Logic(object):
    def __init__(self, players: list[player.Player], settings: st.Settings):
        self._scores = {player:0 for player in players}
        self._settings = settings
        self._game_done = False
        pass
        
    def start_game(self):
        """
        Execute a full game.
        """
        while self._game_done is False:
            self._play_round()
            interface.show_final_end_round_data(self._scores, 
                self._settings.max_points)
            self._game_done = True
            keep_going = 0
            for s in self._scores.values():
                if s < self._settings.max_points:
                    keep_going += 1
                    if keep_going == 2:
                        # At least 2 people aren't done yet, game is not done
                        self._game_done = False

    def _play_round(self):
        """
        Make each player play turns until the round is done.
        Update players dict with obtained scores.
        """

        num_digits = self._settings.hid_num_len
        possible_digits = self._settings.possible_digits
        
        keep_going = [p for p,s in self._scores.items() 
                        if s < self._settings.max_points]

        # Generate a hidden number per player
        hidden_numbers = {}
        for player in keep_going:
            hidden_numbers[player] = HiddenNumber(num_digits, possible_digits)

        # TODO Code reuse, check abstraction levels
        
        # If collate is on, make each player take a turn at a time until
        # everyone's round is over
        if self._settings.collate is True:
            round_is_done = False
            turn_num = 1
            while round_is_done is False and len(keep_going) > 0:
                keep_going_this_round = keep_going[:]
                for player in keep_going_this_round:
                    interface.show_active_player(player)
                    interface.show_turn(turn_num)
                    guess = player.take_guess(self._settings)
                    bulls, cows = hidden_numbers[player].get_matches(guess)
                    interface.guess_result(bulls, cows)

                    if bulls == self._settings.hid_num_len:
                        # Hidden number discovered
                        keep_going.remove(player)
                        score = self._settings._get_round_score(turn_num)
                        self._scores[player] += score
                        interface.show_partial_end_round_data(score, 
                            guessed=True)
                    elif turn_num+1 > self._settings.max_turns:
                        # Time is up
                        score = self._settings._get_round_score(turn_num, 
                            guessed=False)
                        self._scores[player] += score
                        interface.show_partial_end_round_data(score, 
                            guessed=False,
                            hidden_num=hidden_numbers[player].reveal())

                turn_num += 1
                if turn_num > self._settings.max_turns:
                    round_is_done = True
            return
        else:
            for player in keep_going:
                interface.show_active_player(player)
                turn_num = 1
                round_is_done = False
                while round_is_done == False:
                    interface.show_turn(turn_num)
                    guess = player.take_guess(self._settings)
                    bulls, cows = hidden_numbers[player].get_matches(guess)
                    interface.guess_result(bulls, cows)

                    if bulls == self._settings.hid_num_len:
                        # Hidden number discovered
                        score = self._settings._get_round_score(turn_num)
                        round_is_done = True
                        interface.show_partial_end_round_data(score, 
                            guessed=True)

                    elif turn_num+1 > self._settings.max_turns:
                        # Time is up
                        round_is_done = True
                        score = self._settings._get_round_score(turn_num,
                            guessed=False)
                        interface.show_partial_end_round_data(score, 
                            guessed=False,
                            hidden_num=hidden_numbers[player].reveal())
                    
                    turn_num += 1
                self._scores[player] += score

    def get_scores(self):
        return sorted(self._scores.items(), key=lambda x: x[1])