# Amazing game made by MoneyTreesMilk and Antokid555

import pygame
import math
import time

#color
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


pygame.mixer.init()
pygame.init()
pygame.display.set_caption('Think of a Name')

font = pygame.font.Font('freesansbold.ttf', 40)

screenW = 1280
screenH = 720
screen = pygame.display.set_mode((screenW, screenH))



#player class
class players(pygame.sprite.Sprite):
	def __init__(self, playertype):
		super(players, self).__init__()
		self.surf = pygame.Surface((50, 50))
		self.rect = self.surf.get_rect()
		self.rect.center = (200, 200)
		self.surf.fill(white)
		self.velocityY1 = 0
		self.velocityY2 = 0
		self.velocityX1 = 0
		self.velocityX2 = 0
		self.friction = 0.2
		self.movementspeed1 = 2
		self.movementspeed2 = 1.7
		self.type = playertype
		self.health = 100
		self.stamina1 = 120
		self.stamina2 = 120
		self.maxspeed1 = 7
		self.maxspeed2 = 6
		self.firstload = False
		self.reach = 1000
		self.angle = 0
		self.damage = 5
		self.knockback = 20
		self.timer1 = 0
		self.timer2 = 0
		self.timer3 = 0



		#movement stuff
	def update(self, pressed_keys, mouseinput):

		self.rect.move_ip((self.velocityX1, self.velocityY1))
		self.rect.move_ip((self.velocityX2, self.velocityY2))

		if not self.firstload:
			self.firstload = True
			if self.type == 'runner':
				self.rect.center = (80, 360)
				self.surf.fill(green)
			if self.type == 'hunter':
				self.rect.center = (1200, 360)

		#things for the runner
		if self.type == 'runner':

			if self.velocityY1 > 0:
				self.velocityY1 = self.velocityY1 - self.friction
			if self.velocityY1 < 0:
				self.velocityY1 = self.velocityY1 + self.friction

			if self.velocityX1 < 0:
				self.velocityX1 = self.velocityX1 + self.friction
			if self.velocityX1 > 0:
				self.velocityX1 = self.velocityX1 - self.friction


			if pressed_keys[pygame.K_w] and self.velocityY1 > -self.maxspeed1:
				self.velocityY1 += -self.movementspeed1
			if pressed_keys[pygame.K_s] and self.velocityY1 < self.maxspeed1:
				self.velocityY1 += self.movementspeed1
			if pressed_keys[pygame.K_a] and self.velocityX1 > -self.maxspeed1:
				self.velocityX1 += -self.movementspeed1
			if pressed_keys[pygame.K_d] and self.velocityX1 < self.maxspeed1:
				self.velocityX1 += self.movementspeed1
			if pressed_keys[pygame.K_SPACE] and self.stamina1 > 0:
				if self.stamina1 > 0:
					self.maxspeed1 = 10
					self.movementspeed1 = 3
					self.stamina1 -= 1
				if self.stamina1 <= 0:
					self.movementspeed1 = 2
					self.maxspeed1 = 7
			if pressed_keys[pygame.K_SPACE] == False and self.stamina1 < 120:
				self.stamina1 += 0.2
				self.stamina1 = round(self.stamina1, 2)
				self.maxspeed1 = 7

			pygame.draw.rect(screen, white, (0, 0, 300, 30))
			pygame.draw.rect(screen, red, (0, 0, self.health * 3, 30))

			pygame.draw.rect(screen, white, (0, 30, 240, 10))
			pygame.draw.rect(screen, blue, (0, 30, self.stamina1 * 2, 10))
			


			healthtxt = font.render('Health', True, white)
			staminatxt = font.render('Stamina', True, white)
			screen.blit(healthtxt, (310, 0))
			screen.blit(staminatxt, (310, 40))

			if self.health <= 0:
				game.gamestate = 3
			
		if self.timer3 >= 15:
			self.damage += 5
			self.timer3 = 0

		#things for the hunter
		if self.type == 'hunter':

		

			if self.velocityY2 > 0:
				self.velocityY2 = self.velocityY2 - self.friction
			if self.velocityY2 < 0:
				self.velocityY2 = self.velocityY2 + self.friction

			if self.velocityX2 < 0:
				self.velocityX2 = self.velocityX2 + self.friction
			if self.velocityX2 > 0:
				self.velocityX2 = self.velocityX2 - self.friction


			if pressed_keys[pygame.K_UP] and self.velocityY2 > -self.maxspeed2:
				self.velocityY2 += -self.movementspeed2
			if pressed_keys[pygame.K_DOWN] and self.velocityY2 < self.maxspeed2:
				self.velocityY2 += self.movementspeed2
			if pressed_keys[pygame.K_LEFT] and self.velocityX2 > -self.maxspeed2:
				self.velocityX2 += -self.movementspeed2
			if pressed_keys[pygame.K_RIGHT] and self.velocityX2 < self.maxspeed2:
				self.velocityX2 += self.movementspeed2
			if mouseinput[2] and self.stamina2 > 0:
				if self.stamina2 > 0:
					self.maxspeed2 = 9
					self.movementspeed2 = 1.8
					self.stamina2 -= 1
				if self.stamina2 <= 0:
					self.movementspeed2 = 1.7
					self.maxspeed2 = 6
			if not mouseinput[2] and self.stamina2 < 120:
				self.stamina2 += 0.2
				self.stamina2 = round(self.stamina2, 2)
				self.maxspeed2 = 6

			pygame.draw.rect(screen, white, (screenW - 120 * 3, 0,screenW - 120 * 3, 30))
			pygame.draw.rect(screen, blue, (screenW - self.stamina2 * 3, 0, self.stamina2 * 3, 30))


			staminatxt2 = font.render('Stamina', True, white)
			screen.blit(staminatxt2, (780, 0))

		timertxt = font.render(f'Time: {self.timer2}', True, white)
		screen.blit(timertxt, (screenW/2 - 60, 0))






		#offscreen prevention
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > screenW:
			self.rect.right = screenW
		if self.rect.bottom > screenH:
			self.rect.bottom = screenH




		if self.timer1 <= 60:
			self.timer1 += 1
		if self.timer1 >= 60:
			self.timer2 += 1
			self.timer1 = 0
			self.timer3 += 1

	def PositionStuff(self):
		self.topright = (self.rect.right, self.rect.top)
		self.topleft = (self.rect.left, self.rect.top)
		self.bottomright = (self.rect.right, self.rect.bottom)
		self.bottomleft = (self.rect.left, self.rect.bottom)

		if self.type == 'hunter':
			if self.topleft[1] > runner.rect.center[1]:
				if self.topleft[0] > runner.rect.center[0]:
					#topleft

					self.reachX = self.topright[0] - runner.rect.center[0]
					self.reachY = self.topright[1] - runner.rect.center[1]
					self.reachX = math.fabs(self.reachX)
					self.reach = self.reachY * self.reachY + self.reachX * self.reachX
					self.reach = math.sqrt(self.reach)
					
					self.angle = self.reachY / self.reach
					self.angle = math.asin(self.angle)
					self.angle = round(self.angle * 180 / math.pi, 1)
					self.quadrent = 2

				elif self.topright[0] < runner.rect.center[0]:
					#topright

					self.reachX = self.topright[0] - runner.rect.center[0]
					self.reachY = self.topright[1] - runner.rect.center[1]
					self.reach = self.reachY * self.reachY + self.reachX * self.reachX
					self.reach = math.sqrt(self.reach)
					
					self.angle = self.reachY / self.reach
					self.angle = math.asin(self.angle)
					self.angle = round(self.angle * 180 / math.pi, 1)
					self.quadrent = 1

			elif self.bottomleft[1] < runner.rect.center[1]:
				if self.bottomleft[0] > runner.rect.center[0]:
					#bottomleft

					self.reachX = self.topright[0] - runner.rect.center[0]
					self.reachY = self.topright[1] - runner.rect.center[1]
					self.reach = self.reachY * self.reachY + self.reachX * self.reachX
					self.reach = math.sqrt(self.reach)
					
					self.angle = self.reachY / self.reach
					self.angle = math.asin(self.angle)
					self.angle = math.fabs(round(self.angle * 180 / math.pi, 1))
					self.quadrent = 3

				elif self.bottomright[0] < runner.rect.center[0]:
					#bottomRight

					self.reachX = self.topright[0] - runner.rect.center[0]
					self.reachY = self.topright[1] - runner.rect.center[1]
					self.reach = self.reachY * self.reachY + self.reachX * self.reachX
					self.reach = math.sqrt(self.reach)
					
					self.angle = self.reachY / self.reach
					self.angle = math.asin(self.angle)
					self.angle = math.fabs(round(self.angle * 180 / math.pi, 1))
					self.quadrent = 4

	def DamageCheck(self, mouseinput):
		if self.type == 'runner':
			if pygame.sprite.spritecollide(self, Hunterhit, False) and hunter.reach < 200:
				self.health -= self.damage

				if hunter.quadrent == 1:
					self.knockbackY = round(self.knockback * math.sin(hunter.angle / 180 * math.pi), 2)
					self.knockbackX = self.knockback * self.knockback - self.knockbackY * self.knockbackY
					self.velocityY1 -= self.knockbackY
					self.velocityX1 += math.sqrt(self.knockbackX)
				
				elif hunter.quadrent == 2:
					self.knockbackY = round(self.knockback * math.sin(hunter.angle / 180 * math.pi), 2)
					self.knockbackX = self.knockback * self.knockback - self.knockbackY * self.knockbackY
					self.velocityY1 -= self.knockbackY
					self.velocityX1 -= math.sqrt(self.knockbackX)

				elif hunter.quadrent == 3:
					self.knockbackY = round(self.knockback * math.sin(hunter.angle / 180 * math.pi), 2)
					self.knockbackX = self.knockback * self.knockback - self.knockbackY * self.knockbackY
					self.velocityY1 += self.knockbackY
					self.velocityX1 -= math.sqrt(self.knockbackX)

				elif hunter.quadrent == 4:
					self.knockbackY = round(self.knockback * math.sin(hunter.angle / 180 * math.pi), 2)
					self.knockbackX = self.knockback * self.knockback - self.knockbackY * self.knockbackY
					self.velocityY1 += self.knockbackY
					self.velocityX1 += math.sqrt(self.knockbackX)



class MouseBox(pygame.sprite.Sprite):
	def __init__(self):
		super(MouseBox, self).__init__()
		self.image = pygame.Surface((30, 30))
		self.image.fill(black)
		self.surf = self.image
		self.rect = self.image.get_rect()
		self.firstload = False


	def update(self):
		self.rect.center = pygame.mouse.get_pos()

		if not self.firstload:
			self.firstload = True
			Hunterhit.add(self)


class PlayButton(pygame.sprite.Sprite):
	def __init__(self):
		super(PlayButton, self).__init__()
		self.image = pygame.Surface((200, 50))
		self.image.fill((100, 100, 100))
		self.surf = self.image
		self.rect = self.image.get_rect()
		self.rect.center = (screenW/2, screenH/2)

	def update(self):
		if pygame.sprite.spritecollide(self, Hunterhit, False):
			game.gamestate = 2


playbtn = PlayButton()


class Game():
	def __init__(self):
		self.gamestate = 1
		self.time = 0
		self.time2 = 0


	def titlescreen(self):
		screen.fill(blue)
		screen.blit(playbtn.surf, playbtn.rect)

		playtxt = font.render('play', True, red)
		screen.blit(playtxt, (screenW/2 - 30, screenH/2 - 20))
		Mouse.update()
		playbtn.update()


	def maingame(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		pressed_keys = pygame.key.get_pressed()
		mouse_press = pygame.mouse.get_pressed(num_buttons=3)

		if pressed_keys[pygame.K_ESCAPE]:
			running = False


		for thing in AllSprites:
			screen.blit(thing.surf, thing.rect)

		runner.update(pressed_keys, mouse_press)
		hunter.update(pressed_keys, mouse_press)
		hunter.PositionStuff()
		Mouse.update()

	def endscreen(self):
		runner.firstload = False
		hunter.firstload = False
		screen.fill(black)
		endtxt = font.render(f'time was: {hunter.timer2}   L', True, white)
		screen.blit(endtxt, (screenW/2 - 140, screenH/2 - 20))
		runner.health = 100
		self.time += 1
		if self.time > 600:
			self.gamestate = 1
			hunter.timer2 = 0
			runner.timer2 = 0



	def checkstate(self):
		if self.gamestate == 1:
			self.titlescreen()
		if self.gamestate == 2:
			self.maingame()
		if self.gamestate == 3:
			self.endscreen()




game = Game()


AllSprites = pygame.sprite.Group()
Hunterhit = pygame.sprite.Group()

runner = players('runner')
hunter = players('hunter')
Mouse = MouseBox()


AllSprites.add(runner)
AllSprites.add(hunter)






#gameloop
clock = pygame.time.Clock()
running = True
while running:
	screen.fill(black)



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False	
		if event.type == pygame.MOUSEBUTTONDOWN:
			runner.DamageCheck(mouse_press)

	pressed_keys = pygame.key.get_pressed()
	mouse_press = pygame.mouse.get_pressed(num_buttons=3)

	if pressed_keys[pygame.K_ESCAPE]:
		running = False



	game.checkstate()


	pygame.display.flip()
	clock.tick(60)

pygame.quit()
