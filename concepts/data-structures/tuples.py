"""
Tuples
 - ordered
 - immutable
 - allows duplicte elements
"""


nums = [1,2,3,4,5]

# tuple definition
items = ('Tony', 30, 'Maryland')

single = ('Alone',)


# convert list to tuple
convert = tuple(nums)


# lenght of tuple
lenght = len(items)


# count elements
counter = items.count('Tony')


# find index
first = items.index(30)


# access
item = items[-1]


# iteration
for i in items:
    print(i)


# check for element
if 30 in items:
    print('Found')


# unpack
name, age, state = items