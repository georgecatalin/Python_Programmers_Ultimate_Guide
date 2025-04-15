a = 1978
b = 1954

print("a =",a, "\tb=",b)

print("swap the values")

(a,b) = (b,a)
print("a =",a, "\tb=",b)

# how does this work? does it contradict the immutability of tuples? No
# it does not modify any tuple, it just unpacks (a,b) and creates a new tuple by reassigning a = b , b = a

