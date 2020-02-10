# CubeDraftModeHelper for Magic: The Gathering
The goal of this small Python algorithm is to help you find the best draft parameters for a cube draft.
By that, I mean the number of packs, their size, and the burn amount (amount of cards we discard per pack) according to the number of players and the cube size you set.

# How do I define the "best parameters"?
In this program the best parameters are those that provide a draft experience that is as close as possible to a classic 8 players draft (3 packs of 15 per player).
Currently to translate this concept, I look at two calculated values:
- The average quantity of unique cards per pick - best value defined as 8 as it's the one you get with a classic 8 players draft.
Unique means you have not already seen them. It defines the selection you will have for each pick and therefore the amont of synergies/how focused your deck is on average.
- The amount of times packs wheel - best value defined as 2 so that you see each pack exactly 2 times

# Initial Parameters
The initial parameters are the number of packs per player, their size and the number of players.
They use some constants like the size of the cube (360 by default).
The program will generate all the possible initial parameters given some values and filters which have a default value but which you can adjust.
It will then sort them according to how close their two relevant calculated values are to the ideal values.

# Repl.it
You can try this program out here:
- Execute: https://CubeDraftHelper.maximebastion.repl.run
- See code: https://repl.it/@MaximeBastion/CubeDraftHelper
