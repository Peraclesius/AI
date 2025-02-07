INITIAL_STATE = '.........'

def successor(state, index, player):
    return state[:index] + player + state[index+1:]

def legal_moves(state):
    return [i for i in range(len(state)) if state[i] == '.']

def winner(state):
    pass

