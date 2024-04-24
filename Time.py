from datetime import datetime

now = datetime.now() # current date and time




def today_date():
    return [int(now.strftime("%Y")),int(now.strftime("%m")),int(now.strftime("%d")),int(now.strftime("%H")),int(now.strftime("%M")),int(now.strftime("%S"))]

def add_times(og_time,added_time):
    newtime = [0,0,0,0,0,0]
    newtime[5] = og_time[5] + added_time[5]
    while newtime[5] > 60:
        newtime[5] += -60
        newtime[4] += 1
    newtime[4] = og_time[4] + added_time[4]
    while newtime[4] > 60:
        newtime[4] += -60
        newtime[3] += 1
    newtime[3] = og_time[3] + added_time[3]
    while newtime[3] > 60:
        newtime[3] += -60
        newtime[2] += 1    

    newtime[2] = og_time[2] + added_time[2]
    newtime[1] = og_time[1] + added_time[1]
    newtime[0] = og_time[0] + added_time[0]
    
    while (newtime[1] == 1 and newtime[2] > 31) or 





print(today_date())