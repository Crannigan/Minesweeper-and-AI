import pygame

class tile:
	xPos = 0
	yPos = 0
	state = 0
	width = 0
	height = 0
	tileIMG = 0
	nearBombs = 0
	isBombId = False
	isFlag = False
	clicked = False
	def __init__(self, x, y, w, h, screen):
		self.xPos = x
		self.yPos = y
		self.width = w
		self.height = h
		self.screen = screen
		self.gray = (128,128,128)
		self.lightGray = (169,169,169)
		self.black = (0,0,0)


	def buildBackground(self):
		self.myTileLines = pygame.draw.rect(self.screen, self.black,(self.xPos,self.yPos,self.width,self.height))
		self.myTile = pygame.draw.rect(self.screen, self.gray,(self.xPos + 3,self.yPos + 3,self.width - 4,self.height - 4))
		if(self.isBombId and self.clicked == 1):
			self.addBombAction()
		elif(self.clicked and (not self.isBombId) and (not self.isFlag)):
			self.addClickedAction()
		elif(self.isFlag):
			self.addFlagAction()


	def addBomb(self):
		if(self.isBombId):
			return False
		else:
			self.isBombId = True
			return True

	def isBomb(self):
		return self.isBombId

	def addBombAction(self):
		self.tileIMG = pygame.image.load('images/bomb.png')
		self.tileIMG = pygame.transform.scale(self.tileIMG, (self.width - 4, self.height - 4))
		rect = self.tileIMG.get_rect()
		rect = rect.move((self.xPos + 3, self.yPos + 3))
		self.screen.blit(self.tileIMG, rect)


	def updateAndPrint(self, tileX, tileY, tileWidth, tileHeight):
		self.xPos = tileX
		self.yPos = tileY
		self.width = tileWidth
		self.height = tileHeight
		self.buildBackground()

		return self


	def clickedTile(self):
		self.clicked = 1
		return self.isBombId

	def addFlagAction(self):
		self.flagIMG = pygame.image.load('images/flag.png')
		self.flagIMG = pygame.transform.scale(self.flagIMG, (self.width - 4, self.height - 4))
		rect = self.flagIMG.get_rect()
		rect = rect.move((self.xPos + 3, self.yPos + 3))
		self.screen.blit(self.flagIMG, rect)

	def placeFlag(self):
		if not(self.clicked):
			self.isFlag = (not self.isFlag)


	def addClickedAction(self):
		self.lightTile = pygame.draw.rect(self.screen, self.lightGray, (self.xPos + 3, self.yPos + 3, self.width + 4, self.height - 4))

		if not(self.nearBombs == 0):
			self.myFont = pygame.font.SysFont('Comic Sans MS', 50)
			textsurface = self.myFont.render(str(self.getNumNearBombs()), False, (0, 0, 0))
	
			self.screen.blit(textsurface,((self.xPos + (self.width // 2) - (textsurface.get_width() // 2)),self.yPos))


	def setNearBombs(self, val):
		self.nearBombs = val

	def getNumNearBombs(self):
		return self.nearBombs


	def clickedBomb(self):
		self.clicked = 1

	def isClicked(self):
		if(self.clicked == 1):
			return True
		else:
			return False