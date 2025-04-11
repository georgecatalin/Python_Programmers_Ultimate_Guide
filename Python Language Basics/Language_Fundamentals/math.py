import math   # a module is a collection of variables, classes and functions

print("minimum of multiple numbers -> ", min(10,34,7,12)) # minimum of multiple numbers 7
print("maximum of multiple numbers -> ", min(10,34,7,12)) # 34

print("a^b \t ->", pow(10,3)) # 1000

print("ABS(x) ->", abs(46)) # 46
print("ABS(-x) ->", abs(-46)) # 46

print("round(100.3) \t -> ", round(100.3)) # 100
print("round(100.5) \t -> ", round(100.5)) # 100 because Python is even biased
print("round(100.8) \t -> ", round(100.8)) # 101

print("round(101.3) \t -> ", round(101.3)) # 101
print("round(101.5) \t -> ", round(101.5)) # 102 because Python is even biased
print("round(101.8) \t -> ", round(101.8)) # 102

print("math.floor(100.3) \t ->" ,math.floor(100.3))  # 100
print("math.ceil(100.3) \t ->" ,math.ceil(100.3))  # 101

print("math.sqrt(64) \t ->", math.sqrt(64)) # 8
print("math.pi \t -> ", math.pi) #3.1415...
print("math.factorial(7) \t ->", math.factorial(7))

print("round(134.45452) \t ->", round(134.45452,2)) # 134.45
print("round(134.4370) \t ->", round(134.4370,2)) # 134.44
print("round(134.4350) \t ->", round(134.4350,2)) # 134.44