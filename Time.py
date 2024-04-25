from datetime import datetime
now = datetime.now() # current date and time
format = ["year","month","day","hour","minut","second"]
years = {0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}
days_in_leap_year = 29
"""note january is month zero"""

def is_leap_year(year):
    return year % 4 == 0

def turn_extra_months_into_normal(months):
    while months > 11:
        months -= 11
    return months

def today_date():
    return [int(now.strftime("%Y")),int(now.strftime("%m")),int(now.strftime("%d")),int(now.strftime("%H")),int(now.strftime("%M")),int(now.strftime("%S"))]

def add_times(og_time,added_time):
    """add the two inputed dates and automaticly sums extras """
    print("fixed")  
    newtime = [0,0,0,0,0,0]
    newtime[5] = og_time[5] + added_time[5]
    newtime[4] = og_time[4] + added_time[4]
    newtime[3] = og_time[3] + added_time[3]
    newtime[2] = og_time[2] + added_time[2]
    newtime[1] = og_time[1] + added_time[1]
    newtime[0] = og_time[0] + added_time[0]
    
    while newtime[5] > 60:
        newtime[5] -= 60
        newtime[4] += 1
    print("fixed")    
    
    while newtime[4] > 60:
        newtime[4] += -60
        newtime[3] += 1
    print("fixed")      
    
    while newtime[3] > 60:
        newtime[3] += -60
        newtime[2] += 1    
    print("fixed")  
    
    while ((newtime[2] > years[turn_extra_months_into_normal(newtime[1])])):
        if is_leap_year(newtime[0]) and newtime[1] == 1:
            newtime[2] += -29
        else:    
            newtime[2] += -years[turn_extra_months_into_normal(newtime[1])]
        newtime[1] += 1
    print("fixed")  

    while newtime[1] > 11:
        newtime[1] += -11
        newtime[0] += 1
    print("fixed")      
    return newtime

def if_larger(a,b):
    """Returns if date a is larger then date b"""

print(add_times([0,0,0,0,0,0],[0,15,1000,100,100,100]))