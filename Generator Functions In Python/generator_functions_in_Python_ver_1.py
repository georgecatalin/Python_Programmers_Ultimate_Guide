# generator functions represent a special type of functions that run-and-pause or return-and-pause

def generator_function():
    print("Started the generator function")
    yield 1953 # execution stops here until rearmed with next(generator_object)
    print("Run the second sequence")
    yield 1954
    print("Run the third sequence")
    yield 1978


generator_object_reference_variable = generator_function()
print("Reference variable for the generator object that was created in the pool of the heap(arena)", generator_object_reference_variable)

# at this moment , only the generator object was created, the function was not executed
print(next(generator_object_reference_variable)) # returns 1953 and executes up to the first yield statement
print(next(generator_object_reference_variable)) # returns 1954 and executes up to the second yield statement
print(next(generator_object_reference_variable)) # return 1978 and executes upt to the third yield statement
print("***")
