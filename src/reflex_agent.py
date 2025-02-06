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

'''
visited: {(0, 1):True}
offset_list = [('north', (0, 1)), ('east', (1, 0)), ('south', (0, -1)), ('west', (-1, 0))]

if we have not visited the location, set it as visited. 
if there is dirt, clean.
now, we want to attemp to find out whether or not were at at a wall or not. 
if we have not visited the locations around us, pick one and move. check percept
if there is no dirt we know that we hit a wall and didn't move. mark as wall

'''
# visited = {}
# location = (0, 0)

# def old_state_agent(percept):
#     global location, visited
#
#     #mark visited locations
#     if location not in visited:
#         visited[location] = True
#
#     #clean if there is dirt
#     if percept:
#         return 'clean'
#
#     # collect possible moves
#     possible_moves = []
#     for direction, offset in OFFSETS.items():
#         new_x, new_y = location[0] + offset[0], location[1] + offset[1]
#
#         #check unexplored locations first
#         if (new_x, new_y) not in visited:
#             possible_moves.append((direction, (new_x, new_y)))
#
#     #if there are unexplored moves, move there
#     if possible_moves:
#         move, new_location = random.choice(possible_moves)
#     else:
#         move, new_location = random.choice(list(OFFSETS.items()))
#         new_location = (location[0] + new_location[0], location[1] + new_location[1])
#     # ensure we don't hit walls or go out of bounds
#     if new_location in visited and new_location :
#         return random.choice(['north', 'south', 'east', 'west'])
#
#     # update state
#     location = new_location
#     visited[location] = True
#     return move


# Track visited locations and detected walls
visited = {}
location = (0, 0)  # Start unknown
walls = {}
wallCheck = False
past_location = (0, 0)
def state_agent(percept):
    global visited, location, walls, wallCheck, past_location

    if percept:
        return 'clean'

    if wallCheck:
        wallCheck = False
        location = past_location


    possible_moves = []
    possible_NonWallsMoves = []
    for direction, offset in OFFSETS:
        new_x, new_y = location[0] + offset[0], location[1] + offset[1]
        possible_NonWallsMoves.append((direction, (new_x, new_y)))
        if (new_x, new_y) not in visited and (new_x, new_y) not in walls:
            possible_moves.append((direction, (new_x, new_y)))
        elif (new_x, new_y) in walls:
            possible_NonWallsMoves.remove((direction, (new_x, new_y)))
            wallCheck = True

    if possible_moves:
        past_location = location
        move, location = random.choice(possible_moves)

    else:
        move, location = random.choice(possible_NonWallsMoves)

    return move







def state_agent_reset():
    global visited, location
    visited = {}
    location = (0, 0)
    walls = {}
    wallcheck = False


run(20, 50000, state_agent)
# print(many_runs(20, 50000, 10, random_agent))
# print(many_runs(20, 50000, 10, state_agent, state_agent_reset))