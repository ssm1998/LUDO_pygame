import LUDOfunctions
class player:
    '''This class keeps on updating the status of the player'''
    def __init__(self, color = '', order = 0):
        self.color = color
        self.order = order


players = playerSpecify()
count = 1
for var in players:
    if players[var] != '':
        if count == 1:
            player1 = player(players[var],1)
            count += 1
        elif count == 2:
            player2 = player(players[var],2)
            count += 1
        elif count == 3:
            player3 = player(players[var],3)
            count += 1
        elif count == 4:
            player4 = player(players[var],4)
            count += 1

