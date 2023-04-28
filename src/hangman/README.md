You have to implement a class Hangman that receives a word in it's constructor and has the method guess, that will be used by the player to try to guess the word.

Your method guess will receive a letter as parameter and has this return behaviour:

if the player found the word: You found the word! ({word})
if the player got hung: You got hung! The word was {word}.
if the game still on: {game state}
if the game has ended already: The game has ended.
important: if the player guesses a letter that was already guessed, you should ignore it and return the {game state}

{game state}
The {game state} is the word to be found with all letters separated by white space. The letters that weren't found yet will be replaced with _ and, if the player had missed one or more letters, we will keep this record adding # to the output followed by a string with all missed letters in order of occurence.

Ex. If the player is trying to guess the word codewars and attempts with the letters d,w,u,a,c,g,s, respectively, he would guess the letters d,w,a,c,s right and miss the letters u,g. The game state at this point should look like:

c _ d _ w a _ s # ug

#Example:

let hangman = new Hangman('wars');

hangman.guess('w')
w _ _ _
hangman.guess('u')
w _ _ _ # u
hangman.guess('s')
w _ _ s # u
hangman.guess('a')
w a _ s # a
hangman.guess('r')
# You found the word! (wars)
hangman.guess('g')
# The game has ended.
