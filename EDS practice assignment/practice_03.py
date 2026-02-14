from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate,"%Y-%m-%d")
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def salary_in_dollor(salary_in_rupees,conversion_rate= 90):
    return salary_in_rupees / conversion_rate

birthdate = input("Enter birthdate(YYYY-MM-DD): ")
salary = float(input("Enter salary in rupees: "))
age = calculate_age(birthdate)
salary_usd = salary_in_dollor(salary)
print(f"Age: {age} years")
print(f"Salary in USD : ${salary_usd:.2f}")
