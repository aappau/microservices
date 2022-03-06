# lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

mult = lambda x,y: x * y
print(mult(7,2))


# sort 
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)


# map
numbers = [1, 2, 3, 4, 5, 6]

my_map = map(lambda x: x*2, numbers)
print(list(my_map))


# filter
my_filter = filter(lambda x: x%2==0, numbers)
print(list(my_filter))
