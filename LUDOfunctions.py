import random

def playerSpecify():
    print "There can only be 2, 3 or 4 players..."
    print "Colors available: Red, Blue, Yellow and Green..." 
    players = input("Enter number of players: ")
    if players == 2:
	color1 = raw_input("Choose color for player 1: ")
	color2 = raw_input("Choose color for player 2: ")
	if color2 == color1:
	    print "Player two can't choose the same color ! Please choose again."
	    color2 = raw_input("Choose color for player 2: ")
	    return color1, color2
    elif players == 3:
	color1 = raw_input("Choose color for player 1: ")
	color2 = raw_input("Choose color for player 2: ")
	if color2 == color1:
	    print "Two players can't choose the same color ! Please choose again."
            color2 = raw_input("Choose color for player 2: ")
        color3 = raw_input("Choose color for player 3: ")
        if color3 == color1 or color3 == color2:
    	    print "Two players can't choose the same color ! Please choose again."
	    color3 = raw_input("Choose color for player 3: ")
	    return color1, color2, color3
    elif players == 4:
	color1 = raw_input("Choose color for player 1: ")
        color2 = raw_input("Choose color for player 2: ")
        if color2 == color1:
            print "Two players can't choose the same color ! Please choose again."
            color2 = raw_input("Choose color for player 2: ")
        color3 = raw_input("Choose color for player 3: ")
        if color3 == color1 or color3 == color2:
            print "Two players can't choose the same color ! Please choose again."
            color3 = raw_input("Choose color for player 3: ")
	color4 = raw_input("Choose color for player 4: ")
	if color4 == color1 or color4 == color2 or color4 == color3:
	    print "Two players can't choose the same color ! Please choose again."
            color4 = raw_input("Choose color for player 4: ")
            return color1, color2, color3, color4
    else:
	playerSpecify()

def startGame():
    '''
    You get to start the game only if you get a six!
    '''
    if random.randint(1,6) == 6:
        print "You got a six ! Start the game !"
        return True


def rollingDie():
    '''
    When the player starts the game after getting a six,
    if the number is anything except six, the player
    gets one move. If it's a six, the player gets to
    roll again. If further the player gets six his/her
    chance is skipped if not, the player gets three
    moves.
    '''
    roll1 = random.randint(1,6)
    print "Roll 1 :", roll1
    if roll1 == 6:
        roll2  = random.randint(1,6)
        print "Roll 2 :", roll2
        if roll2 == 6:
            roll3 = random.randint(1,6)
            print "Roll 3 :", roll3
            if roll3 == 6:
                print "Oops ! Your chance is skipped !"
            else:
                print "Three moves!"
                return roll1,roll2,roll3
        else:
            print "Two moves!"
            return roll1,roll2
    else:
        print "One move!"
        return roll1

print playerSpecify()
