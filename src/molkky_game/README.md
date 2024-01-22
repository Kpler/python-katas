# Introduction
Molkky is a throwing game similar to bowling, where objective is to knock down wooden pins by throwing a wooden stick at them.

# Kata rules

## Setup
There are twelve pins marked from 1 to 12

## Scoring

- Knocking down a pin scores the number of points marked on the pin. If you knock down pin #4, you score 4 points.
- Knocking down several pins scores the number of pins knocked down. If you knock down pins #3, #5 and #8, you score 3 points.
- Scoring above 50 points reduces the score to 25 points. If you have 47 points and score 5 points, you have 25 points.
- Each pin number is unique, you cannot knock down the same pin twice in the same turn.
- At the beginning of a turn, all pins knocked down in the previous turn are reset and are standing again.

## Winning
Game is won when 50 points exactly are reached.

## Losing
Game is lost if no pins are knocked down after three turns.

## Additional rules
- This kata focuses on scoring of 1 single player.
- When a game is won or lost, continuing the game is not possible.
