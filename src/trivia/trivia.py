#!/usr/bin/env python3
import random
from dataclasses import dataclass

from random import randrange
from typing import Optional, List

MAX_PLAYERS = 6


@dataclass
class Player:
    name: str
    place: int = 0
    purse: int = 0
    in_penalty_box: bool = False

    def __str__(self):
        return self.name

    @property
    def is_winner(self):
        return self.purse == 6


class Game:
    def __init__(self):
        self.players: List[Player] = []

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append(self.create_question("Pop", i))
            self.science_questions.append(self.create_question("Science", i))
            self.sports_questions.append(self.create_question("Sports", i))
            self.rock_questions.append(self.create_question("Rock", i))

    @staticmethod
    def create_question(question_type, index):
        return f"{question_type} Question {index}"

    @property
    def is_playable(self):
        return self.how_many_players >= 2

    @property
    def how_many_players(self):
        return len(self.players)

    @property
    def current_player(self):
        return self.players[self.current]

    def add(self, player: Player):
        self.players.append(player)

        print(f"{player} was added")
        print(f"They are player number {len(self.players)}")

        return True

    def roll(self, roll):
        print(f"{self.current_player} is the current player")
        print(f"They have rolled a {roll}")

        if self.current_player.in_penalty_box and not roll % 2 != 0:
            print(f"{self.current_player} is not getting out of the penalty box")
            self.is_getting_out_of_penalty_box = False
            return

        if self.current_player.in_penalty_box and roll % 2 != 0:
            print(f"{self.current_player} is getting out of the penalty box")
            self.is_getting_out_of_penalty_box = True

        self.current_player.place += roll
        if self.current_player.place > 11:
            self.current_player.place -= 12

        print(f"{self.current_player}'s new location is {str(self.current_player.place)}")
        print(f"The category is {self._current_category}")
        self._ask_question()

    def _ask_question(self):
        questions = {
            'Pop': self.pop_questions,
            'Science': self.science_questions,
            'Sports': self.sports_questions,
            'Rock': self.rock_questions
        }
        print(questions[self._current_category].pop(0))

    @property
    def _current_category(self):
        if self.current_player.place % 4 == 0:
            return 'Pop'
        if self.current_player.place % 4 == 1:
            return 'Science'
        if self.current_player.place % 4 == 2:
            return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.current_player.in_penalty_box and not self.is_getting_out_of_penalty_box:
            self.select_next_player()
            return True

        print("Answer was correct!!!!")
        self.current_player.purse += 1
        print(f"{self.current_player} now has {str(self.current_player.purse)} Gold Coins.")
        is_not_winner = not self.current_player.is_winner
        self.select_next_player()
        return is_not_winner

    def wrong_answer(self):
        print(f"Question was incorrectly answered")
        print(f"{self.current_player} was sent to the penalty box")
        self.current_player.in_penalty_box = True
        self.select_next_player()

        return True

    def select_next_player(self):
        self.current += 1
        if self.current == len(self.players):
            self.current = 0


def main(random_seed: Optional[int], player_names: List[str]):

    if random_seed:
        random.seed(random_seed)

    game = Game()
    for name in player_names:
        game.add(Player(name))

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner:
            break


if __name__ == '__main__':
    main(None, ["Chet", "Pat", "Sue"])
