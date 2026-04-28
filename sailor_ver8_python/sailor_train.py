import time
import os
import pdb
import numpy as np
import matplotlib.pyplot as plt
import sailor_funct as sf

# Training data parameters - these may be time-dependent functions:
#alpha = ..................                         # training speed factor
#epsilon = ................                         # exploration factor
#T = ................                               # another exploration method e.g.softmax

#file_name = 'map_small.txt'
#file_name = 'map_easy.txt'
file_name = 'map_simple.txt'
#file_name = 'map_middle.txt'
#file_name = 'map_mid.txt'
#file_name = 'map_big.txt'
#file_name = 'map_spiral.txt'

reward_map = sf.load_data(file_name)
num_of_rows, num_of_columns = reward_map.shape

number_of_episodes = 100*num_of_rows*num_of_columns    # number of training epizodes DO NOT INCREASE!
gamma = 1.0                                            # discount factor

num_of_steps_max = int(4*(num_of_rows + num_of_columns))    # maximum number of steps in an episode
Q = np.zeros([num_of_rows, num_of_columns, 4], dtype=float)   # array of <state,action> pairs values
#Q = ......................................................    # maybe random is better
sum_of_rewards = np.zeros([number_of_episodes], dtype=float)

for episode in range(number_of_episodes):
    state = np.zeros([2],dtype=int)                            # initial state here [1 1] but rather random due to exploration
    #state = ....................................

    #print('initial state = ' + str(state) )
    the_end = False
    nr_pos = 0
    while the_end == False:
        nr_pos = nr_pos + 1;                            # move number
      
        # Action choosing (1 - right, 2 - up, 3 - left, 4 - bottom): 
        action = 1
        #action = .............................................. 

        state_next, reward  = sf.environment(state, action, reward_map); 
      
        # State-action value modification:
        # Q = ................................................
        
        #print('state = ' + str(state) + ' action = ' + str(action) +  ' -> next state = ' + str(state_next) + ' reward = ' + str(reward))

        state = state_next;      # going to the next state
      
        # end of episode if maximum number of steps is reached or last column
        # is reached
        if (nr_pos == num_of_steps_max) | (state[1] >= num_of_columns-1):
            the_end = True;                                  
      
        sum_of_rewards[episode] += reward
    if episode % 500 == 0:
        print('episode = ' + str(episode) + ' average sum of rewards = ' + str(np.mean(sum_of_rewards)))
#print('average sum of rewards = ' + str(np.mean(sum_of_rewards)))

strategy = np.ones((num_of_rows, num_of_columns)) # for now
#strategy = .........................................................

mean_sum_of_rewards = sf.sailor_test(reward_map, strategy, 5000, gamma)
sf.draw(reward_map,strategy,mean_sum_of_rewards)
