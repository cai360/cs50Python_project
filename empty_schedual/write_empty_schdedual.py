from calendar import Calendar
import datetime 
import time
import csv
import shift

def main():
    s = shift.Shift()
    c = Calendar()
    #(day_number, week_number)
    empty_calendar = c.monthdays2calendar(2024, 12)
    

    #delete day 0
    new_calendar = []
    for i in range(len(empty_calendar)):
        for j in range(7):
            if empty_calendar[i][j][0]  != (0):
                new_calendar.append(empty_calendar[i][j])
    
    #use for write the row on the file
    calendar_day = []
    for i in range(len(new_calendar)):
           calendar_day.append(new_calendar[i][0])
    calendar_day.insert(0, "time")

    schedual = {}
    schedual.update( {calendar_day[i] : None} )
    
            
 
    work_hours = s.generate(8,16)
    with open("empty_file.csv", mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(calendar_day)
        writer.writerows(work_hours)
               

if __name__ == "__main__":
    main()
