months_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}


print()

print(f"Dictionary sorted by keys: \n{sorted(months_days.items())}")

print()

print(
    f"Dictionary sorted by values: \n{sorted(months_days.items(), key = lambda x: x[1] )}"
)
