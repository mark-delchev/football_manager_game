from datetime import date, timedelta
today = date.today()

for i in range(10):
    future = today + timedelta(days=i)
    print("Future date is:", future)