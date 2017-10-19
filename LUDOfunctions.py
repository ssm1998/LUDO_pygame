mport random

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
