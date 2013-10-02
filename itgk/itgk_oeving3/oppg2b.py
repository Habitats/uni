#! /usr/bin/env python
# itgk oeving 3 - oppg2a

import datetime

monthList = ['January','February','March','April','May','June','July','August','September','October','November','December']
daysList = ['Monday','Tuesday','Wedensday','Thursday','Friday','Saturday','Sunday']

dateInput = raw_input('enter a random date in the format "weekday DD month YYYY":\n> ')
dateList = dateInput.split(' ')

dayName = str(dateList[0])
day = int(dateList[1])
month = str(dateList[2])
year = int(dateList[3])

dayIndex = daysList.index(dayName) + 1
monthIndex = monthList.index(month) + 1

if (dayName in daysList) and (month in monthList) and (0 < day <= 31) and (0 < year <= 9999) and (len(dateList) <= 4):
    x = datetime.date(year,monthIndex,day).isoweekday()
    if x != dayIndex:
        print 'invalid date! maybe the weekday is wrong?'
else:
    print 'invalid date! is the format correct?'
