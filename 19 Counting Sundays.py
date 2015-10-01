import calendar
total = 0
for year in range(1901,2001):
    for month in range(1,13):
        if calendar.weekday(year,month,1) == 6:
            total += 1
print total
