from handle import create_particles
from parameters import *
from ui_elements import *
from graph import *

def on_mouse_down(pos, button):
    if button == 1 and pos[0] >= 150 and pos[0] <=400 and pos[1] >= 200 and pos[1] <= 350 and state['Window'] == 1:
        state['Window'] = 2
        state['Simulation'] = 1
    if button == 1 and pos[0] >= 450 and pos[0] <=700 and pos[1] >= 200 and pos[1] <= 350 and state['Window'] == 1:
        state['Window'] = 2
        state['Simulation'] = 2
    if button == 1 and pos[0] >= 205 and pos[0] <=345 and pos[1] >= 380 and pos[1] <= 420 and state['Window'] == 1:
        graph1()
    if button == 1 and pos[0] >= 505 and pos[0] <=645 and pos[1] >= 380 and pos[1] <= 420 and state['Window'] == 1:
        graph2()  # Def Later
    if button == 1 and pos[0] >= 100 and pos[0] <=170 and pos[1] >= 200 and pos[1] <= 270 and state['Window'] == 2:
        state['RawNum'].append(1)
    if button == 1 and pos[0] >= 200 and pos[0] <=270 and pos[1] >= 200 and pos[1] <= 270 and state['Window'] == 2:
        state['RawNum'].append(2)
    if button == 1 and pos[0] >= 300 and pos[0] <=370 and pos[1] >= 200 and pos[1] <= 270 and state['Window'] == 2:
        state['RawNum'].append(3)
    if button == 1 and pos[0] >= 100 and pos[0] <=170 and pos[1] >= 300 and pos[1] <= 370 and state['Window'] == 2:
        state['RawNum'].append(4)
    if button == 1 and pos[0] >= 200 and pos[0] <=270 and pos[1] >= 300 and pos[1] <= 370 and state['Window'] == 2:
        state['RawNum'].append(5)
    if button == 1 and pos[0] >= 300 and pos[0] <=370 and pos[1] >= 300 and pos[1] <= 370 and state['Window'] == 2:
        state['RawNum'].append(6)
    if button == 1 and pos[0] >= 100 and pos[0] <=170 and pos[1] >= 400 and pos[1] <= 470 and state['Window'] == 2:
        state['RawNum'].append(7)
    if button == 1 and pos[0] >= 200 and pos[0] <=270 and pos[1] >= 400 and pos[1] <= 470 and state['Window'] == 2:
        state['RawNum'].append(8)
    if button == 1 and pos[0] >= 300 and pos[0] <=370 and pos[1] >= 400 and pos[1] <= 470 and state['Window'] == 2:
        state['RawNum'].append(9)
    if button == 1 and pos[0] >= 200 and pos[0] <=270 and pos[1] >= 500 and pos[1] <= 570 and state['Window'] == 2:
        state['RawNum'].append(0)
    if button == 1 and pos[0] >= 300 and pos[0] <=450 and pos[1] >= 500 and pos[1] <= 570 and state['Window'] == 2:
        state['Window'] = 3
        create_particles(state['SpawnNum'])
    if button == 1 and pos[0] >= 5 and pos[0] <=60 and pos[1] >= 5 and pos[1] <= 30 and state['Window'] == 2:
        state['Window'] = 1
    if button == 1 and pos[0] >= 775 and pos[0] <=800 and pos[1] >= 0 and pos[1] <= 17:
        exit()

def drawInterface(screen):
    if state['Window'] == 1:
        draw_main_screen(screen)
    if state['Window'] == 2:
        draw_simulation_ui(screen,state['SpawnNum'])
    if state['Window'] == 3:
        for particle in state['particles']:
            particle.draw(screen)