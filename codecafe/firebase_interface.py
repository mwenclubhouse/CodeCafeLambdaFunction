import os
from typing import List
from firebase import Firebase

from codecafe.player import Player
from codecafe.board import Board


class FirebaseInterface:

    @staticmethod
    def get_config():
        return {
            "apiKey": os.getenv("FIREBASE_API_KEY"),
            "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
            "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
            "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET")
        }

    def __init__(self):
        self.firebase = Firebase(config=FirebaseInterface.get_config())
        self.board = Board()

    def get_database(self):
        return self.firebase.database()

    @staticmethod
    def on_connect():
        instance = FirebaseInterface.shared
        user = Player(instance.board.players, "name")
        doc = os.getenv("PROFILE") if "PROFILE" in os.environ else "main"
        database = instance.get_database()
        database.child(doc).push(user, user.uid)


FirebaseInterface.shared = FirebaseInterface()
