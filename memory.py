from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

taps = 0 # contador de numero de taps

matches = 0 # contador de las parejas encontradas



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    global taps
    taps += 1 # Empieza a contar los taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global matches
        matches += 1 # Empieza a contar las parejas encontradas


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Comenzando en x + 26.8 y y + 1, queda centrado
        goto(x + 26.8, y + 1) 
        #El color se establece dependiento del número del tile que se muestre
        #En RGB se multiplica el valor por una constante para así obtener un color distinto en cada caso
        #En el rojo no se le resta a 255 por la falta de visibilidad
        color(tiles[mark]*5, 255-tiles[mark]*4, 255-tiles[mark]*4)
        #Sin importar dónde empiece se centra, para que el número de dígitos no sea problema
        write(tiles[mark], align = "center", font=('Arial', 30, 'normal')) 

    goto(0,210) # contando contador de taps que se mostrara en pantalla
    write (taps,font=("Arial",20)) # formato en el que se mostrara taps

    if matches == 32: # comparara todas las parejas encontradas con el total de parejas
        up()
        goto(0, 0)
        color('green')
        write("VICTORIA ",  align="center", font=("Arial", 20, "bold")) # Cuando se encuentran todas las parejas, 
                                                                        # muestra un mensaje de victoria
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
colormode(255) #Especificar que se están haciendo modificaciones en RGB
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
