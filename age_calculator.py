import datetime

def calculate_age(birth_date_str):
    try:
        birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        today = datetime.datetime.today().date()
        delta = today - birth_date
        if delta.days < 0:
            raise ValueError("Invalid date. Please enter a valid birthdate.")
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 30)
        return years, months, days
    except ValueError as e:
        print(f"Error: {e}")
        return None, None, None

def main():
    birth_date_input = input("Enter your birthdate in YYYY-MM-DD format: ")
    try:
        years, months, days = calculate_age(birth_date_input)

        print(f"Years: {years}, Months: {months}, Days: {days}")
    except ValueError as e:
        print("Please enter a valid date. All numbers, YYYY-MM-DD format.")

if __name__ == "__main__":
    main()