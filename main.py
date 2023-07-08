from objects import *

n = int(input('Enter number of players: '))
players = []
board = Board()
for i in range(n):
    name = input(f'Enter name for Player {i + 1}:')
    players.append(player(name, i, board))


game = True
while game:
    for p in players:
        game = p.move()