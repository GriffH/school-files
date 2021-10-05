while True:  # https://www.includehelp.com/python/asking-the-user-for-integer-input-in-python-limit-the-user-to-input-only-integer-value.aspx
    try:
        days = int(input("Days after 9/25/2009 :"))  # get # of days
        break
    except ValueError:  # If not integer
        print("Integers Only")
        continue

start = 16637000000  # starting point
speed = 38241
time = days * 24  # time in hours after 9/25

distance = speed * time
distance += start

km = distance * 1.609344
au = distance / 92955887.6
trip = (km * 2 * 1000) / (299792458 * 3600)  # total distance in meters * 2/ speed of light in  meters/hour

print("Voyager is", distance, "miles from the sun.")
print("Voyager is", km, "kilometers from the sun.")
print("Voyager is", au, "Astronomical Units from the sun.")
print("It would take a radio transmission", trip, "hours to travel to voyager and back to Earth")
