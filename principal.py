import pygame
from parqueadero import Estado
import csv

pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode((800, 800))

def Recortar(archivo_img,cr_an,cr_al):
    image= pygame.image.load(archivo_img)
    ancho_img, alto_img=image.get_size()
    lon_x=ancho_img/cr_an
    lon_y=alto_img/cr_al
    m=[]
    for j in range(lon_y):
        fila=[]
        for i in range(lon_x):
            plantilla=image.subsurface(0+(i*cr_an),0+(j*cr_al),cr_an,cr_al)
            fila.append(plantilla)
        m.append(fila)
    return m

def cargar_imagen(nombre,transparente=False):
     try: imagen = pygame.image.load(nombre)

     except pygame.error, message:
          raise SystemExit, message
     imagen = imagen.convert()
     if transparente:
          color = imagen.get_at((0,0))
          imagen.set_colorkey(color, RLEACCEL)
     return imagen
def diccionario():
    file="estados.csv"
    estados=[]
    with open(file) as fh:
        rd = csv.DictReader(fh, delimiter=',') 
        for row in rd:
            estados.append(row)
    return estados

def main():
    fondo = cargar_imagen('fondo.png')
    carro= "carro.png"
    libre="libre.png"
    free=Recortar(libre,78,70)
    car=Recortar(carro,73,67)
    General=pygame.sprite.Group()
    parqueadero_1=Estado(1,[30,20],1,car,free)
    parqueadero_2=Estado(0,[150,20],2,car,free)
    General.add(parqueadero_1)
    General.add(parqueadero_2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
        dicc= diccionario()
        for j in General:
            for i in dicc:
                if int(j.id)== int(i["id"]):
                    j.estado = int(i["estado"])
        screen.blit(fondo, (0, 0))
        General.update()
        General.draw(screen)
        pygame.display.flip()
        
        


if __name__ == '__main__':
    main()