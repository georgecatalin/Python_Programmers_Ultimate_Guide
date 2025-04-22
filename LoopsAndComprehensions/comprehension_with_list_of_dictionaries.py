"""
the syntax of a list comprehension is:
    expression for variable in collection if condition
"""

matches_list = [
    {"player":"George", "score" : 8},
    { "player":"Mara", "score": 7},
    { "player":"Sorina", "score":6},
    { "player":"Liviu", "score": 4},
    { "player": "Sorin", "score":9 }
]

# a comprehension with an expression that does not change any value and no filtering
print([match for match in matches_list])

# a comprehension with an expression that  changes  value and no filtering
print([{**match,"highest_score": 20} for match in matches_list]) # ** is called kwargs

#a comprehension with an expression that  changes avalue and  filtering
print([{**match,"highest_score":50} for match in matches_list if match["score"] >=5])

#a comprehension with an expression that changes value with filtering
print([{**match, "highest_score" : 45, "score" : match["score"] * 3} for match in matches_list if match["score"] >= 6])

#a comprehension that return a list of constant strings
print(["a string" for match in matches_list]) # ['a string', 'a string', 'a string', 'a string', 'a string']

# a comprehension that returns a list of strings
print([match["player"] for match in matches_list if match["score"] >=8])

# a comprehension that returns a boolean
print([match["score"] >= 8 for match in matches_list])

# a comprehension that returns a any()
print(any(match["score"] >= 8 for match in matches_list)) # True

# a comprehension with all()
print(all(match["score"] >= 8 for match in matches_list)) # False

