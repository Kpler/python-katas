# Introduction

Build a simple Zombie Survival engine using Test-Driven Development (TDD).

You control a single survivor trapped in a zombie-infested area.
The game continues until one of the end conditions is met.

## Survivor State

The survivor has the following attributes:

- health → starts at 100
- energy → starts at 100
- zombies_killed → starts at 0
- is_alive → true while health > 0


## Game state

The game tracks:
- total_zombies → total number of zombies in the area
- is_over → whether the game has ended
- score → final score when the game ends

## End conditions

1. Survivor Dies ☠️

- Triggered when health <= 0
- Game ends
- is_alive = false
- score = zombies_killed
- No further actions are allowed

2. Survivor Runs Away 🏃

- Triggered when the survivor chooses to flee
- Game ends immediately
- Survivor may still be alive
- score = zombies_killed
- No further actions are allowed

3. All Zombies Are Killed 🧟‍♂️❌

- Triggered when zombies_killed == total_zombies
- Game ends
- Survivor wins
- score = total_zombies
- No further actions are allowed

# Actions
## fight()

The survivor fights a zombie.

**Rules**:
- Costs 30 energy

- If energy < 30:
the fight fails
the survivor loses 20 health

- If energy ≥ 30:
energy −30
health −10

- zombies_killed +1

## rest()

The survivor rests to recover energy.

**Rules**

- Restores 40 energy
- Energy cannot exceed 100
- Cannot rest if the survivor is dead

## heal()

The survivor uses medical supplies.

**Rules**

- Costs 20 energy
- Restores 25 health
- Health cannot exceed 100
- If energy < 20, nothing happens
- Cannot be used if the game is over

## run_away()

The survivor abandons the fight.

**Rules**

- Game ends immediately
- Survivor may still be alive
- score = zombies_killed
- No further actions are allowed


## Fatal Rules

**If the game is over :**
- No actions can be performed
- all methods become no-ops or raise exceptions based on your design choice.

**health and energy are always between 0 and 100**

## Bonus challenges

- include a bit of randomness in the fight, rest, and heal actions, which could allow 
for property-based testing: instead of mocking randomness, test the properties of the output.
- add difficulty levels that affect the energy and health costs of actions.
- Persistence of high scores 
- Zombie counter UI
- several rounds : the former end game conditions become round end conditions. The survivor can get health
    and energy back to full at the beginning of each round.The game ends when the survivor dies.
- Multiplayer mode : there are several survivors and the game ends when all players are dead. In multiple rounds mode
, a dead survivor won't participate in the next round.
