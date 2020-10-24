from typing import List
from random import random

from codecafe.player import Player

random_questions = [
    "Best Name for a Dog",
    "Best Thing to do at Purdue",
    "Best Name for a programming language"
]


class Board:

    def __init__(self):
        """
        TODO: Create an Empty List of Players
        """
        self.players: List[Player] = []

    @staticmethod
    def get_random_question():
        """
        TODO: find a random question from variable random_question. Return it.
        :return: question from random_question
        """
        random_idx = int(random() * len(random_questions))
        return random_questions[random_idx]

    def get_response(self, ref):
        """
        TODO: iterate through list of players. Get the response to question they selected. DO NOT include the current player question.
        :param ref:
        :return: dict -> {"user reference": "their response"}
        """
        responses = dict()
        for p in self.players:
            response = p.get_response()
            if response is not None and ref != p.uid:
                responses[p.uid] = responses

    def get_result(self):
        """
        TODO: Iterate through list of players. Get answer choice they selected. For each player, select number of players that selected their answer choice.
        return: dict -> {"user reference": 5 (# of users selecting his answer)}
        """
        pass

    def update_scores(self):
        """
        TODO: Based off response from get_result, change the scores of the current players by # of ppl selecting their answer choice / total # of ppl playing * 100.
        NOTE: use player.set_score(new_score) to set the score.
        :return: Nothing
        """
        pass
