import random

class player:
    def __init__(self, name, idn, board) -> None:
        self.name = name
        self.id = idn
        self.pos = 0
        self.board = board
        
        self.hunds = 10
        self.fifs = 10
        self.thous = 4
        self.fithou = 1

        self.bal = 15000
        self.start_pass = 0
        self.started = False
        self.miss_turn = False

    def get_bal(self):
        return self.bal
        # return self.hunds*100 + self.fifs*500 + self.thous*1000 + self.fithou*5000
    
    def roll_die(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'You rolled {die1} + {die2} = {die1 + die2}')
        return die1 + die2
    
    def go_ahead(self, steps):
        self.pos += steps
        if self.pos > 35:
            self.pos = self.pos - 36
        
        self.handle_pos()

    def handle_pos(self, steps):
        cur_pos = self.board.board[self.pos].name
        print(f"You have landed in {cur_pos}")
        print()

        if cur_pos == 'CHANCE':
            print(f'You landed on chance with a {steps}:')
            if steps == 2:
                print('Loss in share market Rs. 2000 :(')
                self.bal -= 2000
            elif steps == 4:
                print('Fine for Drunk Driving! Rs. 1000')
                self.bal -= 1000
            elif steps == 4:
                print('Fine for Drunk Driving! Rs. 1000')
                self.bal -= 1000
            elif steps == 4:
                print('Fine for Drunk Driving! Rs. 1000')
                self.bal -= 1000
            elif steps == 10:
                print('Fine for Drunk Driving! Rs. 1000')
                self.bal -= 1000
            elif steps == 12:
                print('Go to rest house and miss your next turn!')
                self.miss_turn = True
                self.pos = 28
                self.bal -= 100
                print
        

    def move(self):
        print('-'*50)
        print(f"Player {self.id + 1}'s turn:")
        # print(f'''
        # Denomination : Quantity
        #       100 : {self.hunds}
        #       500 : {self.fifs}
        #       1000 : {self.thous}
        #       5000 : {self.fithou}
              
        #       Total : {self.get_bal()}
        #       ''')
        print(f'Balance currently available: {self.get_bal()}')
        input('Press Enter to Roll the Die: ')
        
        roll = self.roll_die()
        if self.pos == 0 and self.started == False:
            # game hasnt started yet
            if roll >= 10:
                self.go_ahead(roll)
                self.started = True
            else:
                print('Sorry you cannot move yet!')
        
        elif self.miss_turn:
            print('You will have to miss this turn!')
            self.miss_turn = False
        else:
            self.go_ahead(roll)

        input("Press Enter to continue...")
        print()
        return True

class Board:
    def __init__(self) -> None:
        self.board_data = [
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
        self.build_board()
    
    def build_board(self):
        self.board = []
        for i in self.board_data:
            self.board.append(Place(i))



class Place:
    def __init__(self, data) -> None:
        l = data.split()
        self.name = l[0]
        self.cost = int(l[1])
        
        if self.cost != 0:
            if l[2] == 'P':
                self.type = 'property'
            else:
                self.type = 'service'
        else:
            self.type = 'special'
        
        self.owner = 'none'
        self.housed = False

    
    def set_owner(self, player):
        self.owner = player.id

    
    def get_rent(self):
        if not self.housed:
            return round(self.cost*0.1/100)*100
        return round(self.cost*0.2/100)*100