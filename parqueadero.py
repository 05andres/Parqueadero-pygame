import pygame
import math
import random
shape_color = (40, 210, 250)
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
ROJO   = (255,   0,   0)

class Estado(pygame.sprite.Sprite):
	def __init__(self,estado,pos,id,sabana,free):
		pygame.sprite.Sprite.__init__(self)
		self.m=0
		self.s=sabana
		self.libre=free[0][0]
		self.image = self.s[self.m][0]
		self.id=id
		self.rect=self.image.get_rect()
		self.estado=estado
		self.rect.x=pos[0]
		self.rect.y=pos[1]
		print "hola"
	def update(self):
		if self.estado == 0:
			self.image = self.libre
		else:
			self.image = self.s[0][0]


	