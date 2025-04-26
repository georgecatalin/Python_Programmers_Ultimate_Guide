list_of_values = []

a = 0
b = 1
list_of_values.extend([a,b])
c = a + b
list_of_values.append(c)

print("The list containing the fibonacci values at this step is {0}.".format(list_of_values))

print()

for i in range(10): # 0 1 2 3 4 5 6 7 8 9
    a = b
    b = c
    c = a + b
    list_of_values.append(c)

print(f"The final list with the fibonacci values is {list_of_values}")