"""
Sets
 - unordered
 - mutable
 - no duplicates
"""


mySet = {1, 2, 3, 4, 1, 2}

newSet = set([2, 2, 4, 5])


# mutation
mySet.add(6)
mySet.add(7)
mySet.discard(3)


# iteration
for i in mySet:
    print(i)

print(mySet)
print(newSet)


odds    = {1, 3, 5, 7, 9}
evens   = {0, 2, 4, 6, 8}
primes  = {2, 3, 5, 7}

# union
u = odds.union(evens)
print(u)


# intersections
i = odds.intersection(primes)
print(i)


# difference
diff = primes.difference(evens)
print(diff)