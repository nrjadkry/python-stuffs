import datetime
# import pytz


x=datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.second)#prints the second
print(x.strftime("%A"))#prints today day
print(x.strftime("%B")) #prints the name of month

today=datetime.date.today()

print(today)

birthday=datetime.date(1998,12,30)
print(birthday)

days_since_birth=today-birthday
print(days_since_birth)





#Adds 10 days to the todays time
tdelta=datetime.timedelta(days=10)
hour_delta=datetime.timedelta(hours=2)
print(today+tdelta) #today is displayed above
print(datetime.datetime.now()+hour_delta)

#datetime.date(y,m,s)
#datetime.time(h,m,s,ms)
#datetime.datetime(y,m,s,h,m,s,ms)


# datetime.datetime.now(tz=pytz.UTC)