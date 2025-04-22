list_secured_marks = [
    {"name":"Chemistry", "secured_mark":8.7},
    {"name":"Maths", "secured_mark":4.7},
    {"name":"Physics", "secured_mark":10.3},
    {"name":"Literature", "secured_mark":4.7},
]


# compute the total sum of the marks, but in case that there exist a mark less than 5.0 abort the calculus

total_marks = 0
for mark in list_secured_marks:
    print(f"{mark["name"]} with {mark["secured_mark"]}")

    if mark["secured_mark"] <= 5.0:
        print(f"I have found a below minimal mark and I skip the computation")
        break

    total_marks += mark["secured_mark"]

print("Total mark", total_marks)