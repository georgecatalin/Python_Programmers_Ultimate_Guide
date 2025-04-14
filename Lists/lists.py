list_1 = [1978, 1953, 1954, 1977, 2011]
print(list_1)
print(type(list_1))

list_heterogeneous = [1978, 3.415, -12, "George"] # as the list stores memory addresses of individual objects in the object pool, there is no limitation about the type of the object
# though in practical usage, one stores a single type of element in a given list

print(list_heterogeneous)
print(type(list_heterogeneous))
print(len(list_heterogeneous)) # number of elements in the list