# Zombie Dice Bots

import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        # A bot that, after the first roll, randomly decides if it will continue or stop
        """
        stopped = False
        while stopped == False:
            random_num = random.randint(0,1)
            if random_num == 0: zombiedice.roll()
            else: stopped = True
        """
        # A bot that stops rolling after it has rolled two shotguns
        """
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
        """
        # A bot that stops rolling after it has rolled two brains
        """
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
        """
        # A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
        """
        count = 1
        shotgun = 0
        while count < 4 and shotgun < 2:
            shotgun += diceRollResults['shotgun']
            diceRollResults = zombiedice.roll()
            count += 1
        """
        # A bot that stops rolling after it has rolled more shotguns than brains
        brains = 0
        shotgun = 0
        while shotgun < brains:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            diceRollResults = zombiedice.roll()
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)