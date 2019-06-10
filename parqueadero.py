import pygame
import math
import random
shape_color = (40, 210, 250)
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
ROJO   = (255,   0,   0)

class Estado(pygame.sprite.Sprite):
	def __init__(self,estado,pos,screen,id,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([50, 20])
		self.image.fill(BLANCO)
		self.image.set_colorkey(BLANCO)
		self.pantalla=screen
		self.color=NEGRO
		self.id=id
		self.rect=self.image.get_rect()
		self.estado=estado
		self.rect.x=pos[0]
		self.rect.y=pos[1]
		self.imagen = imagen.subsurface(72,216,72,72)



		print "hola"

	def update(self):
		if self.estado == 0:
			pass
			#self.color=NEGRO
			#pygame.draw.circle(self.pantalla, self.color,[self.rect.x,self.rect.y], 10)
		else:
			self.pantalla.blit(self.imagen.convert_alpha(), (self.rect.x,self.rect.y))
			#self.color=ROJO
			#pygame.draw.circle(self.pantalla, self.color,[self.rect.x,self.rect.y], 10)


	