# WARRIORS BATTLE GAME

''' Game Sample Output
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game Over
'''


import random
import math

# Warrior & Battle Class
class Warrior:

    # Warriors will have names, health, and attack and block maximums
    def __init__(self, name='Warrior', health=0, maxAtck=0, maxBlck=0):
        self.name = name
        self.health = health
        self.maxAtck = maxAtck
        self.maxBlck = maxBlck

    # They wll have capabilities to attack and block random amounts
    def attack(self):
        # Attack random random() 0.0 to 1.0 * maxAtck + .5
        atckAmount = self.maxAtck * (random.random() + .5)
        return atckAmount

    def block(self):
        # Block will use random()
        blckAmount = self.maxBlck * (random.random() + .5)
        return blckAmount

class Battle:

    def fight(self, warrior1, warrior2):

        # loop until 1 warrier is dead
        # it is unknown how long warriors will fight
        while True:
            # w1 attacks w2
            if self.getAtckRes(warrior1, warrior2) == 'Game over':
                print('Game over')
                break

            # w2 attacks w1
            if self.getAtckRes(warrior2, warrior1) == 'Game over':
                print('Game over')
                break


    # this function does not require self, it is just fine with the warriors
    @staticmethod
    # battle.fight() loop is switching warriors then A, and B will be different
    def getAtckRes(warriorA, warriorB):

        # get warrior A attack
        warriorA_atckAmount = warriorA.attack()

        # get warrior B block
        warriorB_blckAmount = warriorB.block()

        # calculate damage dealt to warrior B
        dmg2warriorB = math.ceil(warriorA_atckAmount - warriorB_blckAmount)

        # update warrior B health
        warriorB.health = warriorB.health - dmg2warriorB

        # print action
        print('{} attacks {} and deals {} damage'
              .format(warriorA.name, warriorB.name, dmg2warriorB))

        # print result
        print('{} is down to {} health'
              .format(warriorB.name, warriorB.health))

        # check attacked warrior is dead or alive
        if warriorB.health <= 0:
            print('{} has Died and {} is Victorious'
                  .format(warriorB.name, warriorA.name))
            return 'Game over'
        else:
            return 'Fight again'


def main():

    # define warrior1 object
    maximus = Warrior('Maximus', 50, 20, 10)
    # define warrior2 object
    galaxon = Warrior('Galaxon', 50, 20, 10)
    # create the battle object
    battle = Battle()
    # start the battle by calling the fight() method
    battle.fight(maximus, galaxon)


main()
