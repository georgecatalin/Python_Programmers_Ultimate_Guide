# ranges are important for executing certain block of code for a number of times

print(range(10)) # range(start, end, step
print(type(range(10))) # <class 'range'>

print(list(range(0,11))) # [0,1,2,3,4,5,6,7,8,9,10]

print(list(range(0,11,2))) # 0,2,4,6,8,10

print(list(range(40,15,-2))) # 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16  # up to but not included 15-> last is 16