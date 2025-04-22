dummy_employees = [
    {"name": "George", "job": "management", "salary": 500},
    {"name": "Alice", "job": "engineering", "salary": 60},
    {"name": "Bob", "job": "design", "salary": 45},
    {"name": "Clara", "job": "marketing", "salary": 55},
    {"name": "David", "job": "support", "salary": 40},
    {"name": "Eva", "job": "management", "salary": 650},
    {"name": "Frank", "job": "engineering", "salary": 70},
    {"name": "Grace", "job": "design", "salary": 50},
    {"name": "Henry", "job": "marketing", "salary": 52},
    {"name": "Ivy", "job": "support", "salary": 48}
]

total_salary = 0

for employee in dummy_employees:

    if employee["job"] == "management": # skip the management jobs for salary sum
        continue

    print(f"The name {employee["name"]} has salary = {employee["salary"]}")


    total_salary += employee["salary"]

print(f"The sum of salaries is {total_salary}")