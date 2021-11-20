from datetime import datetime

#current time using datetime object
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current_time = ",current_time)
