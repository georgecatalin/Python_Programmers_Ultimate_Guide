# nested loops
for i in range(1,8): #  1 2 3 4 5 6 7
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print()
print("*********")

for i in range(1,6): #  1 2 3 4 5
    for j in range(5,i-1,-1):
        print(j, end=" ")
    print()