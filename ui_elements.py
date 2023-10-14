from parameters import *
from pygame import Rect

"All of the definitions of the screen"
def draw_button(screen,x, y, text, size=70, font_size=70, color='black', bg_color='grey'):
    screen.draw.text(text, (x, y), color=color, fontsize=font_size)
    screen.draw.rect(Rect((x - 20, y - 15), (size, size)), bg_color)

def draw_simulation_ui(screen,SpawnNum):#Draws the buttons for number of cells spawned
    draw_button(screen,100, 200, '1')
    draw_button(screen,200, 200, '2')
    draw_button(screen,300, 200, '3')
    draw_button(screen,100, 300, '4')
    draw_button(screen,200, 300, '5')
    draw_button(screen,300, 300, '6')
    draw_button(screen,100, 400, '7')
    draw_button(screen,200, 400, '8')
    draw_button(screen,300, 400, '9')
    draw_button(screen,200, 500, '0')

    screen.draw.text('Enter', (300, 500), color='black', fontsize=50)
    screen.draw.rect(Rect((280, 485), (150, 70)), 'grey')
    screen.draw.text('Home', (10, 10), color='black', fontsize=20)
    screen.draw.rect(Rect((5, 5), (55, 25)), 'grey')
    screen.draw.text('How Many Cells Would You Like to Spawn', (50, 100), color='black', fontsize=40)
    screen.draw.text(str(SpawnNum), (500, 275), color='black', fontsize=50)

def draw_main_screen(screen):
        screen.draw.filled_rect(Rect((0,0),(WIDTH,HEIGHT)),'black')
        for x in range(0, WIDTH, 20):
            for y in range(0, HEIGHT, 20):
                if y % 40 == 0:
                    screen.draw.line((x, y), (x + 20, y + 20), 'white')
                else:
                    screen.draw.line((x + 20, y), (x, y + 20), 'grey')
        for x in range(0, WIDTH, 20):
            for y in range(0, HEIGHT, 20):
                if x % 40 == 0:
                    screen.draw.line((x, y), (x + 20, y + 20), 'white')
                else:
                    screen.draw.line((x + 20, y), (x, y + 20), ('grey'))
        screen.draw.filled_rect(Rect((150,200),(250,150)),(121, 122, 121))
        screen.draw.filled_rect(Rect((450,200),(250,150)),(121, 122, 121))
        screen.draw.rect(Rect((160,210),(230,130)),'black')
        screen.draw.rect(Rect((460,210),(230,130)),'black')

        screen.draw.filled_rect(Rect((200,375),(150,50)),(121, 122, 121))
        screen.draw.filled_rect(Rect((500,375),(150,50)),(121, 122, 121))
        screen.draw.rect(Rect((205,380),(140,40)),'black')#here
        screen.draw.rect(Rect((505,380),(140,40)),'black')#here

        screen.draw.text('simulation 1',(175,260), color = 'black', fontsize=50)#sim 1 text here
        screen.draw.text('simulation 2',(475,260), color = 'black', fontsize = 50)#sim 2 text here
        screen.draw.text('graph: sim 2',(525,390), color = 'black', fontsize = 25)
        screen.draw.text('graph: sim 1',(225,390), color = 'black', fontsize = 25)
        screen.draw.filled_rect(Rect((180,5),(510,55)),'black')
        screen.draw.text('Packing Simulations',(190,10),color = 'grey',fontsize = 70)#Title Text
