# Speed meter vs speeding ticket

driver_speed = float(input("How fast in Km/h were you driving on that street? "))
max_speed = 80

if driver_speed <= 80:
    print("No speeding fine")
elif max_speed < driver_speed <= max_speed + 10:
    print("Got a light speeding ticket")
elif 90 < driver_speed <= max_speed + 20:
    print("Got a serious speeding ticket!")
else:
    print("Got a very serious speeding ticket, you can lose your driver license!!")
