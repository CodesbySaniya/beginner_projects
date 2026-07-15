#dice art game

import Dice_art_game

import random

dice = {
    1: (
        "┌───────┐",
        "│   ●   │",
        "│       │",
        "│       │",
        "└───────┘"
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    )
    # ...
}


roll = random.randint(1,6)

for line in dice[roll]:
  print(roll)
