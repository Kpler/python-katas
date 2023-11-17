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


class Game:
    def __init__(self):
        self.players: List[Player] = []
        self.places = [0] * MAX_PLAYERS
        self.purses = [0] * MAX_PLAYERS
        self.in_penalty_box = [0] * MAX_PLAYERS

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append(self.create_question("Pop", i))
            self.science_questions.append(self.create_question("Science", i))
            self.sports_questions.append(self.create_question("Sports", i))
            self.rock_questions.append(self.create_question("Rock", i))

    @staticmethod
    def create_question(question_type, index):
        return f"{question_type} Question {index}"

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player: Player):
        self.players.append(player)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(f"{player} was added")
        print(f"They are player number {len(self.players)}")

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print(f"{self.players[self.current_player]} is the current player")
        print(f"They have rolled a {roll}")

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.get_place_of_current_player() + roll
                if self.get_place_of_current_player() > 11:
                    self.places[self.current_player] = self.get_place_of_current_player() - 12

                print(f"{self.players[self.current_player]}'s new location is {str(self.get_place_of_current_player())}")
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.get_place_of_current_player() + roll
            if self.get_place_of_current_player() > 11:
                self.places[self.current_player] = self.get_place_of_current_player() - 12

            print(f"{self.players[self.current_player]}'s new location is {str(self.get_place_of_current_player())}")
            print("The category is %s" % self._current_category)
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
        if self.get_place_of_current_player() % 4 == 0:
            return 'Pop'
        if self.get_place_of_current_player() % 4 == 1:
            return 'Science'
        if self.get_place_of_current_player() % 4 == 2:
            return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(f"{self.players[self.current_player]} now has {str(self.purses[self.current_player])} Gold Coins.")

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True
        else:
            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(f"{self.players[self.current_player]} now has {str(self.purses[self.current_player])} Gold Coins.")

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(f"{self.players[self.current_player]} was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)

    def get_place_of_current_player(self):
        return self.places[self.current_player]


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
