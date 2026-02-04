import numpy as np


# update/add code below ...

def ways(cents, coint_types):
    ways_list = [0] * (cents + 1) # list for num ways to make each amount, * with a list multiplies its elements and creates a single line
    ways_list[0] = 1 # one way to make x cents(: use no coins)

    for coin in coint_types:
        for i in range(coin, cents + 1): # start from coin value to cents
            ways_list[i] += ways_list[i - coin] # add ways to make i - coin

    return ways_list[cents]

print(ways(100, [1, 5, 10, 25]))  # Output: 242

names = np.array(['Hannah', 'Astrid', 'Peter', 'Marcus', 'Sofie'])
scores = np.array([85, 92, 78, 90, 88]) 
def lowest_score(names, scores):
    min_index = np.argmin(scores) #numpy.argmin finds the index of the minimum value in the scores array
    lowest_student = names[min_index] #Get the name corresponding to the lowest score
    return lowest_student

print(lowest_score(names, scores))  # Output: Peter

def sort_names(names,scores): 
    sorted_indices = np.argsort(scores) #numpy.argsort returns the indices that would sort the scores array
    sorted_names = names[sorted_indices] #Reorder names based on sorted indices
    return sorted_names
#argsort fun fact: its kind parameter allows you to specify the sorting algorithm
print(sort_names(names, scores))  # Output: ['Peter' 'Hannah' 'Sofie' 'Marcus' 'Astrid']