####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
team_name = 'the meme team'
strategy_name = 'random'
strategy_description = '''
Collude first round. Collude, except in a round after getting 
a severe punishment.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    return random.choice(['c','b'])