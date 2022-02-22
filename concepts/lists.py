"""
Lists
 - ordered
 - mutable
 - allows duplicte elements
"""

# list definition
cars = ['Toyota', 'Honda', 'Ford']
mix = [5, True, 'apple', 'apple']
nums = [3, 5, -2, 5, 6]


# access element 
first = cars[0]
last = cars[-1]


# iteration
for i in mix:
    print(i)


# check for element 
if 'Honda' in cars:
    print('Found')


# length of list
length = len(mix)


# add element to end of list
mix.append('orange')


# add element to specific position
cars.insert(1, 'Benz')


# remove items from list
popped = mix.pop()


# empty list
mix.clear()


# reverse list
cars.reverse()


# sort list
#nums.sort()
sort = sorted(nums)


# concat list
new = cars + nums


# slice
start = nums[:2]
end = nums[2:]
setp = nums[::2]


# list comprehension
multi = [i * i for i in nums]