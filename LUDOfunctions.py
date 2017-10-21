import random,pygame

pygame.init()

#COLORS         R   G   B
WHITE       = (255,255,255)
LIGHTGREEN  = (153,255,153)
GREEN       = ( 51,255, 51)
PINK        = (255,153,204)
RED         = (255, 51, 51)
LIGHTYELLOW = (255,255,153)
YELLOW      = (255,255, 51)
LIGHTBLUE   = (204,255,255)
BLUE        = (  0,128,255)
BLACK       = (  0,  0,  0)

# initialising coin images

greenCoin=pygame.image.load('greencoin.png')
yellowCoin=pygame.image.load('yellowcoin.png')
redCoin=pygame.image.load('redcoin.png')
blueCoin=pygame.image.load('bluecoin.png')


#CONSTANTS
WIDTH = 660   #Change the value of width in order to adjust your screen surface!(should be divisible by 11)
HEIGHT = WIDTH

#Setting up the surface
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LUDO')
gameDisplay.fill(WHITE)

def drawBoard():
	#Setting up the surface
	gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption('LUDO')
	gameDisplay.fill(WHITE)
	
	#Drawing LUDO board
	pygame.draw.polygon(gameDisplay, YELLOW, ((4*(WIDTH/11),4*(WIDTH/11)), (7*(WIDTH/11),4*(WIDTH/11)), (5.5*(WIDTH/11),5.5*(WIDTH/11))))
	pygame.draw.polygon(gameDisplay, GREEN, ((4*(WIDTH/11),4*(WIDTH/11)), (4*(WIDTH/11),7*(WIDTH/11)), (5.5*(WIDTH/11),5.5*(WIDTH/11))))
	pygame.draw.polygon(gameDisplay, RED, ((4*(WIDTH/11),7*(WIDTH/11)), (7*(WIDTH/11),7*(WIDTH/11)), (5.5*(WIDTH/11),5.5*(WIDTH/11))))
	pygame.draw.polygon(gameDisplay, BLUE, ((7*(WIDTH/11),4*(WIDTH/11)), (7*(WIDTH/11),7*(WIDTH/11)), (5.5*(WIDTH/11),5.5*(WIDTH/11))))
	
	#Main Boxes
	pygame.draw.rect(gameDisplay, LIGHTYELLOW, (7*(WIDTH/11),0,4*(WIDTH/11),4*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, LIGHTBLUE, (7*(WIDTH/11),7*(WIDTH/11),4*(WIDTH/11),4*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, LIGHTGREEN, (0,0,4*(WIDTH/11),4*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, PINK, (0,7*(WIDTH/11),4*(WIDTH/11),4*(WIDTH/11)))

	pygame.draw.rect(gameDisplay, YELLOW, (7.5*(WIDTH/11),0.5*(WIDTH/11),3*(WIDTH/11),3*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, BLUE, (7.5*(WIDTH/11),7.5*(WIDTH/11),3*(WIDTH/11),3*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, GREEN, (0.5*(WIDTH/11),0.5*(WIDTH/11),3*(WIDTH/11),3*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, RED, (0.5*(WIDTH/11),7.5*(WIDTH/11),3*(WIDTH/11),3*(WIDTH/11)))

	pygame.draw.rect(gameDisplay, YELLOW, (5*(WIDTH/11),0.5*(WIDTH/11),1*(WIDTH/11),4*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, BLUE, (7*(WIDTH/11),5*(WIDTH/11),3.5*(WIDTH/11),1*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, GREEN, (0.5*(WIDTH/11),5*(WIDTH/11),4*(WIDTH/11),1*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, RED, (5*(WIDTH/11),7*(WIDTH/11),1*(WIDTH/11),3.5*(WIDTH/11)))

	pygame.draw.rect(gameDisplay, YELLOW, (6*(WIDTH/11),0.5*(WIDTH/11),1*(WIDTH/11),0.5*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, BLUE, (10*(WIDTH/11),6*(WIDTH/11),0.5*(WIDTH/11),1*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, GREEN, (0.5*(WIDTH/11),4*(WIDTH/11),0.5*(WIDTH/11),1*(WIDTH/11)))
	pygame.draw.rect(gameDisplay, RED, (4*(WIDTH/11),10*(WIDTH/11),1*(WIDTH/11),0.5*(WIDTH/11)))

	pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(8.25*(WIDTH/11)),int(1.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(9.75*(WIDTH/11)),int(1.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(8.25*(WIDTH/11)),int(2.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(9.75*(WIDTH/11)),int(2.75*(WIDTH/11))),int(0.4*(WIDTH/11)))

	pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(1.25*(WIDTH/11)),int(1.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(2.75*(WIDTH/11)),int(1.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(1.25*(WIDTH/11)),int(2.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(2.75*(WIDTH/11)),int(2.75*(WIDTH/11))),int(0.4*(WIDTH/11)))

	pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(8.25*(WIDTH/11)),int(8.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(9.75*(WIDTH/11)),int(9.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(8.25*(WIDTH/11)),int(9.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(9.75*(WIDTH/11)),int(8.25*(WIDTH/11))),int(0.4*(WIDTH/11)))

	pygame.draw.circle(gameDisplay, PINK, (int(1.25*(WIDTH/11)),int(8.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, PINK, (int(1.25*(WIDTH/11)),int(9.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, PINK, (int(2.75*(WIDTH/11)),int(8.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
	pygame.draw.circle(gameDisplay, PINK, (int(2.75*(WIDTH/11)),int(9.75*(WIDTH/11))),int(0.4*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (int(0.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(0.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(1*(WIDTH/11)),  int(4*(WIDTH/11))),(int(1*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(1.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(1.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(2*(WIDTH/11)),  int(4*(WIDTH/11))),(int(2*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(2.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(2.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(3*(WIDTH/11)),  int(4*(WIDTH/11))),(int(3*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(3.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(3.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(4*(WIDTH/11)),  int(4*(WIDTH/11))),(int(4*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (int(7*(WIDTH/11)),  int(4*(WIDTH/11))),(int(7*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(7.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(7.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(8*(WIDTH/11)),  int(4*(WIDTH/11))),(int(8*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(8.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(8.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(9*(WIDTH/11)),  int(4*(WIDTH/11))),(int(9*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(9.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(9.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(10*(WIDTH/11)), int(4*(WIDTH/11))),(int(10*(WIDTH/11)), int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (int(10.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(10.5*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(0.5*(WIDTH/11))),(7*(WIDTH/11),int(0.5*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(1*(WIDTH/11))),  (7*(WIDTH/11),int(1*(WIDTH/11))),  int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(1.5*(WIDTH/11))),(7*(WIDTH/11),int(1.5*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(2*(WIDTH/11))),  (7*(WIDTH/11),int(2*(WIDTH/11))),  int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(2.5*(WIDTH/11))),(7*(WIDTH/11),int(2.5*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(3*(WIDTH/11))),  (7*(WIDTH/11),int(3*(WIDTH/11))),  int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(3.5*(WIDTH/11))),(7*(WIDTH/11),int(3.5*(WIDTH/11))),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(4*(WIDTH/11))),  (7*(WIDTH/11),int(4*(WIDTH/11))),  int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(7*(WIDTH/11))),   (7*(WIDTH/11),int(7*(WIDTH/11))),   int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(7.5*(WIDTH/11))), (7*(WIDTH/11),int(7.5*(WIDTH/11))), int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(8*(WIDTH/11))),   (7*(WIDTH/11),int(8*(WIDTH/11))),   int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(8.5*(WIDTH/11))), (7*(WIDTH/11),int(8.5*(WIDTH/11))), int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(9*(WIDTH/11))),   (7*(WIDTH/11),int(9*(WIDTH/11))),   int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(9.5*(WIDTH/11))), (7*(WIDTH/11),int(9.5*(WIDTH/11))), int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(10*(WIDTH/11))),  (7*(WIDTH/11),int(10*(WIDTH/11))),  int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(10.5*(WIDTH/11))),(7*(WIDTH/11),int(10.5*(WIDTH/11))),int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (0,5*(WIDTH/11)),(4*(WIDTH/11),5*(WIDTH/11)),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (0,6*(WIDTH/11)),(4*(WIDTH/11),6*(WIDTH/11)),int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (5*(WIDTH/11),0),(5*(WIDTH/11),4*(WIDTH/11)),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (6*(WIDTH/11),0),(6*(WIDTH/11),4*(WIDTH/11)),int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (7*(WIDTH/11),5*(WIDTH/11)),(11*(WIDTH/11),5*(WIDTH/11)),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (7*(WIDTH/11),6*(WIDTH/11)),(11*(WIDTH/11),6*(WIDTH/11)),int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (5*(WIDTH/11),7*(WIDTH/11)),(5*(WIDTH/11),11*(WIDTH/11)),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (6*(WIDTH/11),7*(WIDTH/11)),(6*(WIDTH/11),11*(WIDTH/11)),int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),0),(4*(WIDTH/11),11*(WIDTH/11)),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (7*(WIDTH/11),0),(7*(WIDTH/11),11*(WIDTH/11)),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (0,4*(WIDTH/11)),(11*(WIDTH/11),4*(WIDTH/11)),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (0,7*(WIDTH/11)),(11*(WIDTH/11),7*(WIDTH/11)),int(0.05*(WIDTH/11)))

	pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),4*(WIDTH/11)),(7*(WIDTH/11),7*(WIDTH/11)),int(0.05*(WIDTH/11)))
	pygame.draw.line(gameDisplay, BLACK, (7*(WIDTH/11),4*(WIDTH/11)),(4*(WIDTH/11),7*(WIDTH/11)),int(0.05*(WIDTH/11)))


#initialising positions starting from starting point of green guy
def genPos():
	pos=[(25,450),(75,450),(125,450),(175,450),(225,450),(275,450),(325,450),(375,450),(450,375),(450,325),(450,275),(450,225),(450,175),(450,125),(450,75),(450,25),(550,25),(650,25),(650,75),(650,125),(650,175),(650,225),(650,275),(650,325),(650,375),(725,450),(775,450),(825,450),(875,450),(925,450),(975,450),(1025,450),(1075,450),(1075,550),(1075,650),(1025,650),(975,650),(925,650),(875,650),(825,650),(775,650),(725,650),(650,725),(650,775),(650,825),(650,875),(650,925),(650,975),(650,1025),(650,1075),(550,1075),(450,1075),(450,1025),(450,975),(450,925),(450,875),(450,825),(450,775),(450,725),(375,650),(325,650),(275,650),(225,650),(175,650),(125,650),(75,650),(25,650),(25,550)]
	l=[]
	for i in range(len(pos)):
		l.append(())
		for j in pos[i]:
			l[i]+=(j*660/1100,)
	return l

if __name__ == '__main__':
	pos=genPos()
	print pos


def playerSpecify():
	color1=''
	color2=''
	color3=''
	color4=''
	print "There can only be 2, 3 or 4 players..."
	print "Colors available: Red, Blue, Yellow and Green..." 
	players = int(raw_input("Enter number of players: "))
	if players == 2:
		color1 = raw_input("Choose color for player 1: ")
		color2 = raw_input("Choose color for player 2: ")
		while color2 == color1:
			print "Player two can't choose the same color ! Please choose again."
			color2 = raw_input("Choose color for player 2: ")
		
	elif players == 3:
		color1 = raw_input("Choose color for player 1: ")
		color2 = raw_input("Choose color for player 2: ")
		while color2 == color1:
			print "Two players can't choose the same color ! Please choose again."
			color2 = raw_input("Choose color for player 2: ")
		color3 = raw_input("Choose color for player 3: ")
		while color3 == color1 or color3 == color2:
			print "Two players can't choose the same color ! Please choose again."
			color3 = raw_input("Choose color for player 3: ")
		
	elif players == 4:
		color1 = raw_input("Choose color for player 1: ")
		color2 = raw_input("Choose color for player 2: ")
		while color2 == color1:
			print "Two players can't choose the same color ! Please choose again."
			color2 = raw_input("Choose color for player 2: ")
		color3 = raw_input("Choose color for player 3: ")
		while color3 == color1 or color3 == color2:
			print "Two players can't choose the same color ! Please choose again."
			color3 = raw_input("Choose color for player 3: ")
		color4 = raw_input("Choose color for player 4: ")
		while color4 == color1 or color4 == color2 or color4 == color3:
			print "Two players can't choose the same color ! Please choose again."
			color4 = raw_input("Choose color for player 4: ")
	else:
		playerSpecify()
	return {'player1':color1, 'player2':color2, 'player3':color3, 'player4':color4}

def initCoins(gameDisplay,WIDTH,color1='',color2='',color3='',color4=''):
	'''
	Draws coins in the start squares depending on the color
	'''
	l=[color1,color2,color3,color4]
	countB=0
	countY=0
	countG=0
	countR=0
	if('Yellow' in l):
		gameDisplay.blit(yellowCoin,(825*WIDTH/1100-20,125*WIDTH/1100-28))
		gameDisplay.blit(yellowCoin,(975*WIDTH/1100-20,125*WIDTH/1100-28))
		gameDisplay.blit(yellowCoin,(825*WIDTH/1100-20,275*WIDTH/1100-28)) 
		gameDisplay.blit(yellowCoin,(975*WIDTH/1100-20,275*WIDTH/1100-28))
		countY=4
	if('Blue' in l):
		gameDisplay.blit(blueCoin,(int(8.25*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28))
		gameDisplay.blit(blueCoin,(int(9.75*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28))
		gameDisplay.blit(blueCoin,(int(8.25*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28)) 
		gameDisplay.blit(blueCoin,(int(9.75*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28))
		countB=4
	if('Red' in l):
		gameDisplay.blit(redCoin,(int(1.25*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28))
		gameDisplay.blit(redCoin,(int(1.25*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28))
		gameDisplay.blit(redCoin,(int(2.75*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28))
		gameDisplay.blit(redCoin,(int(2.75*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28))
		countR=4
	if('Green' in l):
		gameDisplay.blit(greenCoin,(int(1.25*(WIDTH/11)-20),int(1.25*(WIDTH/11))-28))
		gameDisplay.blit(greenCoin,(int(2.75*(WIDTH/11)-20),int(1.25*(WIDTH/11))-28))
		gameDisplay.blit(greenCoin,(int(1.25*(WIDTH/11)-20),int(2.75*(WIDTH/11))-28))
		gameDisplay.blit(greenCoin,(int(2.75*(WIDTH/11)-20),int(2.75*(WIDTH/11))-28))
		countG=4
	return [countR,countG,countB,countY]

def updateBoard(countR,countG,countB,countY,gameDisplay,color=''):
	'''
	Moves coins from the square to the start position on the board
	'''
	if(color=='Red'):
		countR-=1
	elif(color=='Yellow'):
		countY-=1
	elif(color=='Blue'):
		countB-=1
	elif(color=='Green'):
		countG-=1
	
	YPos=[[825*WIDTH/1100-20,125*WIDTH/1100-28],[975*WIDTH/1100-20,125*WIDTH/1100-28],
	[825*WIDTH/1100-20,275*WIDTH/1100-28],[975*WIDTH/1100-20,275*WIDTH/1100-28]]
	
	BPos=[[int(8.25*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28],[int(9.75*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28],
	[int(8.25*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28],[int(9.75*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28]]

	RPos=[[int(1.25*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28],[int(1.25*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28],
	[int(2.75*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28],[int(2.75*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28]]

	GPos=[[int(1.25*(WIDTH/11)-20),int(1.25*(WIDTH/11))-28],[int(2.75*(WIDTH/11)-20),int(1.25*(WIDTH/11))-28],
	[int(1.25*(WIDTH/11)-20),int(2.75*(WIDTH/11))-28],[int(2.75*(WIDTH/11)-20),int(2.75*WIDTH/11)-28]]
	
	drawBoard()
	for i in range(countR):
			gameDisplay.blit(redCoin,(RPos[i][0],RPos[i][1]))
	for i in range(countY):
			gameDisplay.blit(yellowCoin,(YPos[i][0],YPos[i][1]))
	for i in range(countB):
			gameDisplay.blit(blueCoin,(BPos[i][0],BPos[i][1]))
	for i in range(countG):
			gameDisplay.blit(greenCoin,(GPos[i][0],GPos[i][1]))
	pygame.display.flip()
	
	if(color=='Red'):
		gameDisplay.blit(redCoin,pos[-17])
		position=-17
	elif(color=='Yellow'):
		gameDisplay.blit(yellowCoin,pos[17])
		position=17
	elif(color=='Blue'):
		gameDisplay.blit(blueCoin,pos[34])
		position=34
	elif(color=='Green'):
		gameDisplay.blit(greenCoin,pos[0])
		position=0
	else:
		position=-1
	print 'updated!'
	pygame.display.flip()
	return (countR,countG,countB,countY,position)

def move(event,coin,color,countR,countG,countB,countY,origPos):
	newPos=origPos
	if(event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE):
		(countR,countG,countB,countY,_)=updateBoard(countR,countG,countB,countY,gameDisplay)
		pygame.display.flip()
		rolls = rollingDie()
		for i in rolls:
			if(i!=6):
				newPos=origPos+i
				if(color=='Red'):
					gameDisplay.blit(redCoin,pos[newPos])
				elif(color=='Yellow'):
					gameDisplay.blit(yellowCoin,pos[newPos])
				elif(color=='Blue'):
					gameDisplay.blit(blueCoin,pos[newPos])
				elif(color=='Green'):
					gameDisplay.blit(greenCoin,pos[newPos])
			else:
				
				if(color=='Red'):
					if(countR>0):
						ans=raw_input('do you want to move a coin or remove another one?new(n)/continue(c):')
						if(ans=='n'):
							(countR,countG,countB,countY,position)=updateBoard(countR,countG,countB,countY,gameDisplay,color)
							newPos=origPos
						else:
							gameDisplay.blit(redCoin,pos[origPos+i])
							newPos=origPos+i
					else:
						gameDisplay.blit(redCoin,pos[origPos+i])
						newPos=origPos+i
				if(color=='Yellow'):
					if(countY>0):
						ans=raw_input('do you want to move a coin or remove another one?new(n)/continue(c):')
						if(ans=='n'):
							newPos=origPos
							(countR,countG,countB,countY,position)=updateBoard(countR,countG,countB,countY,gameDisplay,color)
						else:
							newPos=origPos+i
							gameDisplay.blit(yellowCoin,pos[origPos+i])
					else:
						newPos=origPos+i
						gameDisplay.blit(yellowCoin,pos[origPos+i])
				if(color=='Blue'):
					if(countB>0):
						ans=raw_input('do you want to move a coin or remove another one?new(n)/continue(c):')
						if(ans=='n'):
							newPos=origPos
							(countR,countG,countB,countY,position)=updateBoard(countR,countG,countB,countY,gameDisplay,color)
						else:
							newPos=origPos+i
							gameDisplay.blit(blueCoin,pos[origPos+i])
					else:
						newPos=origPos+i
						gameDisplay.blit(blueCoin,pos[origPos+i])
				if(color=='Green'):
					if(countG>0):
						ans=raw_input('do you want to move a coin or remove another one?new(n)/continue(c):')
						if(ans=='n'):
							newPos=origPos
							(countR,countG,countB,countY,position)=updateBoard(countR,countG,countB,countY,gameDisplay,color)
						else:
							newPos=origPos+i
							gameDisplay.blit(greenCoin,pos[origPos+i])
					else:
						newPos=origPos+i
						gameDisplay.blit(greenCoin,pos[origPos+i])
	pygame.display.flip()
	return (countR,countG,countB,countY,newPos)		



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
				return []
			else:
				print "Three moves!"
				return [roll1,roll2,roll3]
		else:
			print "Two moves!"
			return [roll1,roll2]
	else:
		print "One move!"
		return [roll1]
