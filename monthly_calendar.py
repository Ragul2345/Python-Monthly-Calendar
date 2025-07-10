import calendar

# Take input from user
year = int(input("Enter year (e.g., 2025): "))
month = int(input("Enter month (1-12): "))

# Display the calendar
print("\nHere is the calendar:")
print(calendar.month(year, month))
