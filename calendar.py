import calendar

print(calendar.weekheader(3))

print(calendar.firstweekday())

#display whole month calendar
print(calendar.month(2019,3))

#dispaly array of all the days
print(calendar.monthcalendar(2019,3))


#print whole calendar of year
print(calendar.calendar(2019))

#print which day is that particular date
day_of_the_week=calendar.weekday(2019,3,8)
print(day_of_the_week)

is_leap=calendar.isleap(2019)
print(is_leap)

#count the number of leap days between these years
how_many_leap_days=calendar.leapdays(2000,2005)
print(how_many_leap_days)
