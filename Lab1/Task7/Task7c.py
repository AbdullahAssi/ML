import datetime

current_date = datetime.date.today()

current_time = datetime.datetime.now().time()

print("Current Date:", current_date)

# Converted time into 12-hour format
time_12hour = current_time.strftime("%I:%M:%S %p")

print("Current Time ", time_12hour)