from datetime import datetime
import math
now = datetime.now() # current date and time
format = ["year","month","day","hour","minut","second"]
years = {0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}
days_in_leap_year = 29
"""note january is month zero"""

def is_leap_year(year):
    return year % 4 == 0

def turn_extra_months_into_normal(months):
    while months > 11:
        months -= 11 * math.floor(months/11)
    return months

def today_date():
    return [int(now.strftime("%Y")),int(now.strftime("%m")),int(now.strftime("%d")),int(now.strftime("%H")),int(now.strftime("%M")),int(now.strftime("%S"))]

def add_times(og_time,added_time):
    """add the two inputed dates and automaticly sums extras """ 
    newtime = [0,0,0,0,0,0]
    newtime[5] = og_time[5] + added_time[5]
    newtime[4] = og_time[4] + added_time[4]
    newtime[3] = og_time[3] + added_time[3]
    newtime[2] = og_time[2] + added_time[2]
    newtime[1] = og_time[1] + added_time[1]
    newtime[0] = og_time[0] + added_time[0]
    
    if newtime[5] > 60:
        slit = math.floor(newtime[5]/60)
        newtime[5] -= slit * 60
        newtime[4] += slit 
        print(1)   
    
    if newtime[4] > 60:
        slit = math.floor(newtime[4]/60)
        newtime[4] -= 60 * slit
        newtime[3] += slit
        print(2) 
    
    if newtime[3] > 24:
        slit = math.floor(newtime[3]/24)
        newtime[3] -= 24 * slit
        newtime[2] += slit 
        print(3)    

    #if a day is grater then the months aloted days in the month it will auto fix that
    while ((newtime[2] > years[turn_extra_months_into_normal(newtime[1])])):
        if is_leap_year(newtime[0]) and newtime[1] == 1:
            newtime[2] += -29
        else:    
            newtime[2] += -years[turn_extra_months_into_normal(newtime[1])]
        newtime[1] += 1
        print(4) 

    if newtime[1] > 11:
        slit = math.floor(newtime[1]/11)
        newtime[1] -= 11 * slit
        newtime[0] += slit 
        print(3) 
    
    return newtime

def is_larger(a,b):
    """Returns if date a is larger then date b"""
    try:
        if a[0] > b[0]:
            return True
        elif a[0] < b[0]:
            return False
        elif a[1] > b[1]:
            return True
        elif a[1] < b[1]:
            return False
        elif a[2] > b[2]:
            return True
        elif a[2] < b[2]:
            return False
        elif a[3] > b[3]:
            return True
        elif a[3] < b[3]:
            return False
        elif a[4] > b[4]:
            return True
        elif a[4] < b[4]:
            return False
        elif a[5] > b[5]:
            return True
        elif a[5] < b[5]:
            return False
        else:
            return False
    except:
        print("Error you fucked up")