"""
If the mark > 80 , then grade = 'A'
mark >=60  and mark <80 then grade = 'B'
mark >= 40 and mark < 60 then grade = 'C'
mark < 40 then grade = 'Failed'
"""

secured_mark = int(input("Enter your mark: "))
grade = None

if secured_mark >= 80:
    grade = "A"
elif secured_mark >= 60 and secured_mark < 80:
    grade = "B"
elif secured_mark >= 40 and secured_mark < 60:
    grade = "C"
else:
    grade = "Failed"

print(grade)