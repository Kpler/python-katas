ou have to implement a class Hangman that receives a word in it's constructor and has the method guess, that will be used by the player to try to guess the word.

Your method guess will receive a letter as parameter and has this return behaviour:

if the player found the word: You found the word! ({word})
if the player got hung: You got hung! The word was {word}.
if the game still on: {game state}
if the game has ended already: The game has ended.
important: if the player guesses a letter that was already guessed, you should ignore it and return the {game state}
