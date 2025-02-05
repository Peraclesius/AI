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


def state_agent(percept):
    global location, visited

    # If this location is new, mark it as visited
    if location not in visited:
        visited[location] = True

        # If there's dirt, clean it
    if percept:
        return 'clean'

    # Check unexplored neighboring locations
    possible_moves = []
    for direction, offset in OFFSETS.items():
        new_x, new_y = location[0] + offset[0], location[1] + offset[1]

        if (new_x, new_y) not in visited:
            possible_moves.append((direction, (new_x, new_y)))

    if possible_moves:
        # Pick an unexplored move
        move, new_location = random.choice(possible_moves)
    else:
        # If all surrounding locations are explored, move randomly
        move, new_location = random.choice(list(OFFSETS.items()))
        new_location = (location[0] + new_location[0], location[1] + new_location[1])

    # Attempt to move
    location = new_location  # Update assumed location

    # Mark new location as visited
    visited[location] = True
    return move


def state_agent_reset():
    global visited, location
    visited = {}
    location = (0, 0)





run(20, 50000, state_agent)
# print(many_runs(20, 50000, 10, random_agent))
# print(many_runs(20, 50000, 10, state_agent, state_agent_reset))