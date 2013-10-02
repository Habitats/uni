#! /usr/bin/env python
# itgk oeving 3 - oppg2a

import datetime

dt = 0

dateInput = raw_input('enter a random date in the format YYYY.MM.DD:\n> ')
dateList = dateInput.split('.')
dt = datetime.date(int(dateList[0]),int(dateList[1]),int(dateList[2]))

monthList = ['January','February','March','April','May','June','July','August','September','October','November','December']
daysList = ['Monday','Tuesday','Wedensday','Thursday','Friday','Saturday','Sunday']

print 'The entered date is: %s %s. %s %s' % (daysList[dt.weekday()],dateList[2], monthList[int(dateList[1])-1], dateList[0])
