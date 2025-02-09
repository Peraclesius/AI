#Elliot Mayer
import random
from vacuum import *

def reflex_agent(percept):
    if percept:
        return 'clean'
    else:
        return 'north'


def random_agent(percept):
    if percept:
        return 'clean'
    else:
        return random.choice(['north', 'south', 'east', 'west'])


# Track visited locations and detected walls
visited = set()
location = (0, 0)  # Start unknown
walls = set()
wallCheck = False
past_location = (0, 0)
def state_agent(percept):
    global visited, location, walls, wallCheck, past_location

    if percept:
        past_location = location
        wallCheck = False
        return 'clean'

    if wallCheck:
        wallCheck = False
        walls.add(location)
        location = past_location

    visited.add(location)

    possible_moves = []
    possible_NonWallsMoves = []
    for direction, offset in OFFSETS.items():
        new_x, new_y = location[0] + offset[0], location[1] + offset[1]
        if (new_x, new_y) not in walls:
            possible_NonWallsMoves.append((direction, (new_x, new_y)))
        if (new_x, new_y) not in visited and (new_x, new_y) not in walls:
            possible_moves.append((direction, (new_x, new_y)))

    if possible_moves:
        past_location = location
        move, location = random.choice(possible_moves)
        wallCheck = True

    else:
        move, location = random.choice(possible_NonWallsMoves)
        wallCheck = False

    return move


def state_agent_reset():
    global visited, location, walls, wallCheck
    visited = set()
    location = (0, 0)
    walls = set()
    wallCheck = False


run(20, 50000, state_agent)
# print(many_runs(20, 50000, 10, random_agent))
# print(many_runs(20, 50000, 10, state_agent, state_agent_reset))