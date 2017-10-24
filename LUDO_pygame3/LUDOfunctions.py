import random,pygame

pygame.init()

#classes

class player:
	'''This class keeps on updating the status of the player'''
	def __init__(self, color,number,pos,width,started=False):
		self.color = color
		self.started=started
		self.number=number
		self.coins=[]
		for i in range(4):
			self.coins.append(coin(color,self.number,i+1,pos,width))

class coin:
	def __init__(self,color,player,number,pos,width):
		self.color=color
		self.player=player
		self.number=number
		self.positionIn=0
		self.position=0
		if(self.color=='Green'):
			
			self.pos=pos
			self.posIn=[]
			for i in range(7):
				self.posIn.append([pos[i][0],pos[i][1]+width/11])

		elif(self.color=='Red'):
			
			self.pos=pos[51:68]+pos[:51]
			self.posIn=[]
			for i in range(7):
				self.posIn.append([pos[i][0]+width/11,pos[i][1]])
			
		elif(self.color=='Blue'):
			
			self.pos=pos[34:68]+pos[:34]
			self.posIn=[]
			for i in range(7):
				self.posIn.append([pos[i][0],pos[i][1]-width/11])
		elif(self.color=='Yellow'):
			
			self.pos=pos[17:68]+pos[:17]
			self.posIn=[]
			for i in range(7):
				self.posIn.append([pos[i][0]-width/11,pos[i][1]])
		

	def move(self,roll,display):
		self.position=self.position+roll
		if(self.position<68):
			display.blit(eval(self.color+"Coin"),self.pos[self.position])
		else:
			if(self.positionIn==0):
				self.positionIn=68-self.position
			else:
				self.positionIn=self.positionIn+roll
			if(self.positionIn<7):
				display.blit(eval(self.color+"Coin"),self.posIn[self.positionIn])

	def draw(self,display):
		if(self.position<68):
			display.blit(eval(self.color+"Coin"),self.pos[self.position])
		else:
			display.blit(eval(self.color+"Coin"),self.posIn[self.positionIn])


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

GreenCoin=pygame.image.load('greencoin.png')
YellowCoin=pygame.image.load('yellowcoin.png')
RedCoin=pygame.image.load('redcoin.png')
BlueCoin=pygame.image.load('bluecoin.png')


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
			l[i]+=(j*WIDTH /1100,)
	return l
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
	return (color1, color2, color3, color4)

def initCoins(gameDisplay,WIDTH,color1='',color2='',color3='',color4=''):
	'''
	Draws coins in the start squares depending on the color
	'''
	l=[color1,color2,color3,color4]
	countB=0
	countY=0
	countG=0
	countR=0
	players=[]
	if('Yellow' in l):
		gameDisplay.blit(YellowCoin,(825*WIDTH/1100-20,125*WIDTH/1100-28))
		gameDisplay.blit(YellowCoin,(975*WIDTH/1100-20,125*WIDTH/1100-28))
		gameDisplay.blit(YellowCoin,(825*WIDTH/1100-20,275*WIDTH/1100-28)) 
		gameDisplay.blit(YellowCoin,(975*WIDTH/1100-20,275*WIDTH/1100-28))
		countY=4
	if('Blue' in l):
		gameDisplay.blit(BlueCoin,(int(8.25*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28))
		gameDisplay.blit(BlueCoin,(int(9.75*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28))
		gameDisplay.blit(BlueCoin,(int(8.25*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28)) 
		gameDisplay.blit(BlueCoin,(int(9.75*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28))
		countB=4
	if('Red' in l):
		gameDisplay.blit(RedCoin,(int(1.25*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28))
		gameDisplay.blit(RedCoin,(int(1.25*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28))
		gameDisplay.blit(RedCoin,(int(2.75*(WIDTH/11)-20),int(8.25*(WIDTH/11))-28))
		gameDisplay.blit(RedCoin,(int(2.75*(WIDTH/11)-20),int(9.75*(WIDTH/11))-28))
		countR=4
	if('Green' in l):
		gameDisplay.blit(GreenCoin,(int(1.25*(WIDTH/11)-20),int(1.25*(WIDTH/11))-28))
		gameDisplay.blit(GreenCoin,(int(2.75*(WIDTH/11)-20),int(1.25*(WIDTH/11))-28))
		gameDisplay.blit(GreenCoin,(int(1.25*(WIDTH/11)-20),int(2.75*(WIDTH/11))-28))
		gameDisplay.blit(GreenCoin,(int(2.75*(WIDTH/11)-20),int(2.75*(WIDTH/11))-28))
		countG=4
	
	for i in l:
		if(i!=''):
			players.append(player(i,l.index(i)+1,pos,WIDTH))
	return [countR,countG,countB,countY,players]

def getStarted(player,countR,countG,countB,countY):
	'''
	Moves coins from the square to the start position on the board
	'''
	if(player.color=='Red' and countR!=0):
		countR-=1
	elif(player.color=='Yellow' and countY!=0):
		countY-=1
	elif(player.color=='Blue' and countB!=0):
		countB-=1
	elif(player.color=='Green' and countG!=0):
		countG-=1
	print (countR,countG,countB,countY)
	return (countR,countG,countB,countY)

def updateBoard(countR,countG,countB,countY,gameDisplay,players):
	'''
	redraws the bard with all the coins after they have moved to their respective positions
	'''
	
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
			gameDisplay.blit(RedCoin,(RPos[i][0],RPos[i][1]))
	for i in range(countY):
			gameDisplay.blit(YellowCoin,(YPos[i][0],YPos[i][1]))
	for i in range(countB):
			gameDisplay.blit(BlueCoin,(BPos[i][0],BPos[i][1]))
	for i in range(countG):
			gameDisplay.blit(GreenCoin,(GPos[i][0],GPos[i][1]))
	pygame.display.flip()
	
	for i in players:
		if(i.color=='Red'):
			for j in range(4-countR):
				i.coins[j].draw(gameDisplay)
		if(i.color=='Blue'):
			for j in range(4-countB):
				i.coins[j].draw(gameDisplay)
		if(i.color=='Green'):
			for j in range(4-countG):
				i.coins[j].draw(gameDisplay)
		if(i.color=='Yellow'):
			for j in range(4-countY):
				i.coins[j].draw(gameDisplay)
		
	print 'updated!'
	pygame.display.flip()
	

def move(event,player,countR,countG,countB,countY,players):
	if(event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE):
		
		pygame.display.flip()
		rolls = rollingDie()
		for i in rolls:
			if(i!=6):
				if(player.color=='Red'):
					if(countR<=2):
						print "enter the coin number which you want to move from ",range(4-countR)
						n=input()
						player.coins[n].move(i,gameDisplay)
					else:
						player.coins[0].move(i,gameDisplay)
				if(player.color=='Yellow'):
					if(countY<=2):
						print "enter the coin number which you want to move from ",range(4-countY)
						n=input()
						player.coins[n].move(i,gameDisplay)
					else:
						player.coins[0].move(i,gameDisplay)
				if(player.color=='Green'):
					if(countG<=2):
						print "enter the coin number which you want to move from ",range(4-countG)
						n=input()
						player.coins[n].move(i,gameDisplay)
					else:
						player.coins[0].move(i,gameDisplay)
				if(player.color=='Blue'):
					if(countB<=2):
						print "enter the coin number which you want to move from ",range(4-countB)
						n=input()
						player.coins[n].move(i,gameDisplay)
					else:
						player.coins[0].move(i,gameDisplay)
				
			else:
				
				if(player.color=='Red'):
					if(countR>0):
						ans=raw_input('do you want to move a coin or remove another one?new(n)/continue(c):')
						if(ans=='n'):
							countR,countG,countB,countY=getStarted(player,countR,countG,countB,countY)
							updateBoard(countR,countG,countB,countY,gameDisplay,players)
							
						else:
							if(countR<=2):
								print "enter the coin number which you want to move from ",range(4-countR)
								n=input()
								player.coins[n].move(i,gameDisplay)
							else:
								player.coins[0].move(i,gameDisplay)
					else:
						print "enter the coin number which you want to move from ",range(4-countR)
						n=input()
						player.coins[n].move(i,gameDisplay)
				if(player.color=='Yellow'):
					if(countY>0):
						ans=raw_input('do you want to move a coin or remove another one?new(n)/continue(c):')
						if(ans=='n'):
							countR,countG,countB,countY=getStarted(player,countR,countG,countB,countY)
							updateBoard(countR,countG,countB,countY,gameDisplay,players)
							
						else:
							if(countY<=2):
								print "enter the coin number which you want to move from ",range(4-countY)
								n=input()
								player.coins[n].move(i,gameDisplay)
							else:
								player.coins[0].move(i,gameDisplay)
					else:
						print "enter the coin number which you want to move from ",range(4-countY)
						n=input()
						player.coins[n].move(i,gameDisplay)
				if(player.color=='Blue'):
					if(countB>0):
						ans=raw_input('do you want to move a coin or remove another one?new(n)/continue(c):')
						if(ans=='n'):
							countR,countG,countB,countY=getStarted(player,countR,countG,countB,countY)
							updateBoard(countR,countG,countB,countY,gameDisplay,players)
							
						else:
							if(countB<=2):
								print "enter the coin number which you want to move from ",range(4-countB)
								n=input()
								player.coins[n].move(i,gameDisplay)
							else:
								player.coins[0].move(i,gameDisplay)
					else:
						print "enter the coin number which you want to move from ",range(4-countB)
						n=input()
						player.coins[n].move(i,gameDisplay)
				if(player.color=='Green'):
					if(countG>0):
						ans=raw_input('do you want to move a coin or remove another one?new(n)/continue(c):')
						if(ans=='n'):
							countR,countG,countB,countY=getStarted(player,countR,countG,countB,countY)
							updateBoard(countR,countG,countB,countY,gameDisplay,players)
							
						else:
							if(countG<=2):
								print "enter the coin number which you want to move from ",range(4-countG)
								n=input()
								player.coins[n].move(i,gameDisplay)
							else:
								player.coins[0].move(i,gameDisplay)
					else:
						print "enter the coin number which you want to move from ",range(4-countR)
						n=input()
						player.coins[n].move(i,gameDisplay)
	updateBoard(countR,countG,countB,countY,gameDisplay,players)
	pygame.display.flip()
	return (countR,countG,countB,countY,player)		



def startGame(event):
	'''
	You get to start the game only if you get a six!
	'''
	if(event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE):
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


