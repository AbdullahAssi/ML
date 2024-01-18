from datetime import datetime, timedelta

present_date = datetime.now()
days_to_add = 145
future_date = present_date + timedelta(days=days_to_add)

print("Present date:", present_date.strftime("%Y-%m-%d"))
print("Future date:", future_date.strftime("%Y-%m-%d"))
