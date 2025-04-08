my_string = "computer"

print(my_string[0]) # c
print(my_string[7]) # r

print(my_string[-1]) # r
print(my_string[-2]) # e


#slicing
print("computer"[1]) #o
print(my_string[2:5]) # mpu -> starts from [2] not including [5]
print(my_string[-6:-3]) # mpu  starts from [-6] not including [-3]
print(my_string[:4]) # comp -> starts from 0 not including 4
print(my_string[4:]) # uter -> starts from [4] till the end
print(my_string[4:20]) # uter -> starts from [4] till the last character, because its index is less than [20] no index out of range

print(my_string[:4] + "hopa" + my_string[4:]) # comphopauter