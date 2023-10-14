import pgzrun
from handle import run_sim1,run_sim2
from interface import *

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    drawInterface(screen)
    
def update():
    #Put this somewhere else later
    if state['Window'] == 2:
        state['SpawnNum'] = ''.join(str(num) for num in state['RawNum'])

    if state['Window'] == 3 and state['Simulation'] == 1:
        run_sim1()
    if state['Window'] == 3 and state['Simulation'] == 2:
        run_sim2()


    

pgzrun.go()