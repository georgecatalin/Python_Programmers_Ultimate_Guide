funny_quotes = [
    "I'm not lazy, I'm on energy-saving mode.",
    "404: Motivation not found.",
    "I would agree with you, but then we’d both be wrong.",
    "Why do Java developers wear glasses? Because they don’t C#.",
    "Python: where the snakes are friendly and indentation is law.",
    "I told my computer I needed a break… it said 'Error 404: Life not found'.",
    "Running code is fun... until the bugs start running too.",
    "Coffee: because adulting is hard.",
    "My code doesn’t bug, it develops unexpected features.",
    "Ctrl + S is my love language.",
    "I write Python, because typing semicolons is a waste of calories.",
    "There’s no place like 127.0.0.1",
    "Zombies use brains… I debug without one.",
    "First I drink the coffee, then I do the things… eventually.",
    "Why test in production? Because it works on my machine!"
]

# lists are: ordered, indexed, mutable and duplicatable
# tuples are: ordered, indexed, immutabable and duplicatable

# the elements of the list are called as : items, elements or objects

# access the elements of the list by forward indexing
print("The length of the list is ", len(funny_quotes))
print(funny_quotes[0]) #  "I'm not lazy, I'm on energy-saving mode."
print(funny_quotes[2]) # "I would agree with you, but then we’d both be wrong."
print(funny_quotes[14]) #  "Why test in production? Because it works on my machine!"

# access the elements of the list by backward indexing
print(funny_quotes[-1]) #  "Why test in production? Because it works on my machine!"
print(funny_quotes[-14]) # "404: Motivation not found."
print(funny_quotes[-15]) #   "I'm not lazy, I'm on energy-saving mode."

# slicing lists
print(funny_quotes[2:5])
# [ "I would agree with you, but then we’d both be wrong.", "Why do Java developers wear glasses? Because they don’t C#.",  "Python: where the snakes are friendly and indentation is law."]

print(funny_quotes[:2])
print(funny_quotes[12:])