names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names,dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)


orders = ['daisies', 'periwinkle']
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)
new_orders = orders + ["lilac","iris"]

#get the length of the list
list1_len = len(orders)
print(list1_len)

print(orders[0])
#Print the second-last element
print(orders[-2])

#Slices
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[-2:]

#Count
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count("Jake")
print(jake_votes)

#Sort
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

#sorted (like sort but returns)
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print(games_sorted)
