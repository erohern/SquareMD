from particles import Particle,Square
from parameters import *
import random

def create_particles(SpawnNum):
    if state['Simulation'] == 1:
        state['particles'].extend([Particle(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), COLORS[4]) for _ in range(int(SpawnNum))])
    else:
        state['particles'].extend([Square(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), COLORS[4]) for _ in range(int(SpawnNum))])

def particles_in_neighboring_cells(grid, cell_x, cell_y):
    neighboring_cells = [
        (cell_x, cell_y),
        (cell_x+1, cell_y), (cell_x-1, cell_y),
        (cell_x, cell_y+1), (cell_x, cell_y-1),
        (cell_x+1, cell_y+1), (cell_x-1, cell_y-1),
        (cell_x+1, cell_y-1), (cell_x-1, cell_y+1),
    ]

    for cx, cy in neighboring_cells:
        if (cx, cy) in grid:
            for particle in grid[(cx, cy)]:
                yield particle


def update_particle_positions(particle):
    # Update particle's position and handle bounce off from the borders
    particle.update()

def create_spatial_partitioning_grid(particles):
    grid = {}
    for particle in particles:
        cell_x = int(particle.x // GRID_SIZE)
        cell_y = int(particle.y // GRID_SIZE)
        grid.setdefault((cell_x, cell_y), []).append(particle)
    return grid


def check_and_resolve_collisions(grid):
    for particle in state['particles']:
        cell_x = int(particle.x // GRID_SIZE)
        cell_y = int(particle.y // GRID_SIZE)

        for other_particle in particles_in_neighboring_cells(grid, cell_x, cell_y):
            if particle is not other_particle and particle.collides_with(other_particle):
                particle.resolve_collision(other_particle)

        update_particle_positions(particle)

def reset_state():
    totalCollide = 0
    packing = 0
    if state['Simulation'] == 1:
        for particle in state['particles']:
            totalCollide += particle.collisions
            packing += ((3.14 * particle.radius**2)/(WIDTH*HEIGHT))

        with open("sim1.txt", "a") as f:
            f.write(str(totalCollide)+','+str(packing))
            f.write('\n')
                
    if state['Simulation'] == 2:
        for particle in state['particles']:
            totalCollide += particle.collisions
            packing += ((particle.size**2)/(WIDTH*HEIGHT))

        with open("sim2.txt", "a") as f:
            f.write(str(totalCollide)+','+str(packing))
            f.write('\n')

    state['Window'] = 2
    state['particles'] = []
    state['RawNum'] = []
    state['SpawnNum'] = 0
    state['tick'] = 0

def run_sim1():
    state['tick'] += 1
    grid = create_spatial_partitioning_grid(state['particles'])
    check_and_resolve_collisions(grid)
    if state['tick'] >= 1000:
        reset_state()

def run_sim2():
    state['tick'] += 1
    grid = create_spatial_partitioning_grid(state['particles'])
    check_and_resolve_collisions(grid)
    if state['tick'] >= 1000:
        reset_state()
    