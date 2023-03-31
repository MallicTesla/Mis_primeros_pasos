import pygame
pygame.init ()

# con esta clase se crean las paredes
class Pared (pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load ("C:\\Pruebas\\Imagenes\\pared01.jpg").convert ()
        # combierte la imajeb rectangulo
        self.rect = self.image.get_rect ()

# la clase es para crear un objeto con la imagen a utilizar del rectangulo
class Bola (pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load ("C:\\Pruebas\\Imagenes\\Raton01.png").convert_alpha () # el convert_alpha es para que el png aparesca con si transparencia
        # combierte la imagen en un rectangulo
        self.rect = self.image.get_rect ()

# se crean los muros
def construir_mapa (mapa) :# se crea una lista de rectangulos a partir de la unlistMuros "mapa"
    listaMuros = []
    x = 0
    y = 0

    for fila in mapa :
        for muro in fila :
            if muro == "x" :
                listaMuros.append(pygame.Rect (x,y,80,80))
            x += 80
        x = 0
        y += 80
    return listaMuros


def dibujar_muro (superfisie, rectangulo) : #   dubuga un rectangulo 
    pygame.draw.rect(superfisie, VERDE, rectangulo)

def dibujar_mapa (superficie, listaMuros) : # se dibuga listaMuros con los rectangulos muro
    for muro in listaMuros :
        dibujar_muro (superficie, muro)

ANCHO = 1280
ALTO = 720
movil = pygame.Rect(600,400, 40,40)

x = 0
y = 0
lateral = 0
vertical = 0

NEGRO = (0,0,0)
VERDE = (0,255,0)

# se crea el display pasandole el ancho y el verticalo  
ventana = pygame.display.set_mode((ANCHO, ALTO))
# se pone el nombre a la ventana
pygame.display.set_caption ("Muro")
# se inisioa el reloj 
reloj = pygame.time.Clock ()

# se crea la lista listaPared
listaPared = pygame.sprite.Group ()
pared = Pared ()
listaPared.add (pared)

# se crea la lista listaBola
listaBola = pygame.sprite.Group ()
bola = Bola ()
listaBola.add (bola)

# mapa del laberipto
mapa = [
"xxxxxxxxxxxxxxxx",
"x              x",
"x xxx xxxxxxxx x",
"x x   x        x",
"x xx xxxxx xxx x",
"x              x",
"xxxxxxx xxxx  xx",
"x              x",
"xxxxxxxxxxxxxxxx"
]

listaMuros = construir_mapa (mapa)

# el while esta atento para cuando ay una interacsion
gameOver = False
while not gameOver :
    reloj.tick (60)

    # es para etectar los eventos de la pantalla 
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            gameOver = True

        # detecta los eventos del teclado que teclas se pulsan (en este csao detecta las flechas)

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                lateral =-5

            elif event.key == pygame.K_RIGHT :
                lateral =+5

            elif event.key == pygame.K_UP :
                vertical =-5

            elif event.key == pygame.K_DOWN :
                vertical =+5

        else :
            lateral = 0
            vertical = 0

#   se crea un rectangulo
    movil.x += lateral
    movil.y += vertical

#   ase que el rectangulo se mueve con las flechas
    bola.rect.x = movil.x
    bola.rect.y = movil.y

# se crea una colicion 

    # for muro in listaMuros : # se recrea cada cuadro de la lista para comprobar las colisiones
    #     if movil.colliderect (muro) :
    #         movil.x -= lateral
    #         movil.y -= lateral

# asi se crea una colision y evita que se desplase hacia los lados cuando colisiona
    for muro in listaMuros :
        if movil.colliderect(muro):
            if lateral > 0:
                movil.right = muro.left
            elif lateral < 0:
                movil.left = muro.right
            if vertical > 0:
                movil.bottom = muro.top
            elif vertical < 0:
                movil.top = muro.bottom

    # fondo
    ventana.fill (NEGRO)

# dibugando

    x = 0
    y = 0
    for fila in mapa :
        for muro in fila :
            if muro == "x":
                pared.rect.x = x
                pared.rect.y = y
                listaPared.add (pared)
                listaPared.draw (ventana)

            x += 80
        x = 0
        y += 80
    listaBola.draw (ventana)
    # dibujar_mapa (ventana, listaMuros)
    pygame.display.flip ()

pygame.quit ()


# lo vi en https://www.youtube.com/watch?v=9ZkPsDXzrB0&ab_channel=fpred