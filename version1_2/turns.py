from datetime import date, timedelta
today = date.today()

# Generating dates from current date to current date + i
for i in range(10):
    future = today + timedelta(days=i)
    print("Future date is:", future)
