import settings as st
import interface

class Player(object):
    """
    Abstract class. Instance subclasses HumanPlayer or ComputerPlayer instead.
    """
    id = 1
    def __init__(self):
        self._id = Player.id
        Player.id += 1
        
    def take_guess(self, settings: st.Settings):
        """
        Abstract method, to be implemented by subclasses.
        """
        raise NotImplementedError

    def __str__(self):
        return f"Player nº{self._id}"

class HumanPlayer(Player):
    def take_guess(self, settings: st.Settings):
        """
        Make the player take a guess.
        Return a valid guess.
        """
        return interface.human_take_guess(*settings.hid_num_cons)
        

class ComputerPlayer(Player):
    def take_guess(self, settings: st.Settings):
        pass
    def __str__(self) -> str:
        return "Computer player"
    """
    Plus a few private methods that call the appropiate AI functions.
    """