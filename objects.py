import random

class player:
    def __init__(self, name, idn) -> None:
        self.name = name
        self.id = idn
        self.pos = 0
        
        self.hunds = 10
        self.fifs = 10
        self.thous = 4
        self.fithou = 1

        self.bal = self.get_bal()

    def get_bal(self):
        return self.hunds*100 + self.fifs*500 + self.thous*1000 + self.fithou*5000
    
    def roll_die(self):
        die1 = random.randint(1, 12)
        die2 = random.randint(1, 12)
        print(f'You rolled {die1} + {die2} = {die1 + die2}')
        return die1 + die2

class Board:
    def __init__(self) -> None:
        self.board = [
            'START 0 S',
            'MUMBAI 8500 P',
            'WATER-WORKS 3200 S',
            'RAILWAYS 9500 S',
            'AHMEDABAD 4000 P',
            'INCOME-TAX 0 S',
            'INDORE 1500 P',
            'CHANCE 0 S',
            'JAIPUR 3000 P',
            'JAIL 0 S',
            'DELHI 6000 P',
            'CHANDIGARH 2500 P',
            'ELECTRIC-COMPANY 2500 S',
            'BEST 3500 S',
            'SHIMLA 2200 P',
            'AMRITSAR 3300 P',
            'COMMUNITY-CHEST 0 S',
            'SRINAGAR 5000 P',
            'CLUB 0 S',
            'AGRA 2500 P',
            'CHANCE 0 S',
            'KANPUR 4000 P',
            'PATNA 2000 P',
            'DARJEELING 2500 P',
            'AIR-INDIA 10500 S',
            'KOLKATA 6500 P',
            'HYDERABAD 3500 P',
            'REST-HOUSE 0 S',
            'CHENNAI 7000 P',
            'COMMUNITY-CHEST 0 S',
            'BENGALURU 4000 P',
            'WEALTH-TAX 0 S',
            'MYSORE 2500 P',
            'COCHIN 3000 P',
            'MOTOR-BOAT 5500 S',
            'GOA 4000 P',
        ]