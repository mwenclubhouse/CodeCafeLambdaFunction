from random import random
from typing import List


class Player:

    def __init__(self, current_players: List, name):
        """
        :param current_players: Players Currently Playing
        TODO: Find the average score of people currently playing. Make it into an int, and assign it to player
        TODO: Give a random uid to current player
        TODO: Give a random name to current player. Be fun.
        """
        self.score = sum([player.score for player in current_players])
        self.uid = hash(self.score + name)[:16]
        self.name = name
        self.rand = 0

    """DO NOT TOUCH!"""

    def update_name(self, name):
        pass

    """DO NOT TOUCH!"""

    def set_score(self, new_score):
        pass

    """DO NOT TOUCH"""

    def get_response(self):
        self.rand = int(random() * 2)
        return "random_response" if self.rand == 1 else None

    """DO NOT TOUCH"""

    def get_selected_response(self):
        return self.uid
