from datetime import datetime

def age_calculator():
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    print(f"You are {age} years old.")

age_calculator()
