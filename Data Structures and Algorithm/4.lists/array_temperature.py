numdays = int(input("enter the number of days: "))
total = 0
temps = []
for i in range(1, numdays+1):
    nextday = int(input(f"day {i}'s high temp: "))
    temps.append(nextday)
    total += nextday

avg = round(total/numdays, 2)
print(f"\nAverage = {avg}")

count = 0
for i in temps:
    if i > avg:
        count += 1

print(f"{count} day(s) have temp above average temp.")
