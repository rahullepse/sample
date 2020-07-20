import datetime

a = input('Please Enter Month and Year in comma seperate: ').split(',')

def check_day(month,year):
    date = datetime.date(year,month,13)
    return 'True' if date.strftime('%A') == 'Friday' else 'False'

print(check_day(int(a[0]),int(a[1])))


