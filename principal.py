import pygame
from parqueadero import Estado
import csv

pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode((1233, 600))

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
    fondo = cargar_imagen('arqui.jpg')
    carro= "carro.png"
    libre="libre.png"
    free=Recortar(libre,10,1)
    car=Recortar(carro,73,67)
    Creados = pygame.sprite.Group()
    Borrados = pygame.sprite.Group()
    pos_x=23
    for x in range(1, 16):
        inter=70  
        pos_x+=inter
        anter=pos_x
        parqueadero_1=Estado(0,[pos_x,20],x,car,free,"A")
        Creados.add(parqueadero_1)
    pos_y=70
    for x in range(16, 21):
        inter=70  
        pos_y+=inter
        parqueadero_2=Estado(0,[20,pos_y],x,car,free,"B")
        Creados.add(parqueadero_2)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        dicc= diccionario()
        for j in Creados:
            for i in dicc:
                if int(j.id)== int(i["id"]):
                    j.estado = int(i["estado"])

    

        screen.blit(fondo, (0, 0))
        Creados.update()
        Creados.draw(screen)
        pygame.display.flip()
        
        


if __name__ == '__main__':
    main()