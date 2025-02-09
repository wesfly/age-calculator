import datetime

months = {
    "january": 31,
    "february": 28,
    "march": 30, 
    "april": 31, 
    "may": 30, 
    "june": 31, 
    "july": 30, 
    "august": 31, 
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

date_string = input("Put your date string here: ")
start_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
print(date_string, start_date)

today = datetime.datetime.strptime.today().date()

delta = today - start_date
if delta.days < 0:
    raise ValueError("Invalid date. Please enter a valid date.")

for i in range(1, today - delta.days):
    print("adf")

# def calculate_age(birth_date_str):
#     try:
#         birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
#         today = datetime.datetime.today().date()
#         delta = today - birth_date
#         if delta.days < 0:
#             raise ValueError("Invalid date. Please enter a valid birthdate.")
#         years = delta.days // 365.25
#         months = (delta.days % 365.25) // 30.4
#         days = (delta.days % 30.4)
#         return years, months, days
#     except ValueError as e:
#         error = str(e).split()
#         if "'%Y-%m-%d'" in error:
#             print("Enter a valid date.")
#         else:
#             print(f"Error: {e}")
#         quit()
#         return None, None, None

# def main():
#     birth_date_input = input("Enter your birthdate in YYYY-MM-DD format: ")
#     try:
#         years, months, days = calculate_age(birth_date_input)
        
#         print(f"Years: {int(years)}, Months: {int(months)}, Days: {int(days)}")
#     except ValueError as e:
#         print("Enter a valid date. All numbers, YYYY-MM-DD format.")

# if __name__ == "__main__":
#     main()