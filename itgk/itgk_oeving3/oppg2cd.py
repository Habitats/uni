#! /usr/bin/env python
# itgk oeving 3 - oppg2cd

import datetime

monthList = ['January','February','March','April','May','June','July','August','September','October','November','December']
daysList = ['Monday','Tuesday','Wedensday','Thursday','Friday','Saturday','Sunday']

dateInput = raw_input('enter a random date in the format YYYY.MM.DD:\n> ')
dateList = dateInput.split('.')

year = int(dateList[0])
month = int(dateList[1])
day = int(dateList[2])

christmasDate = datetime.date(year,12,24)
timeLeft = (christmasDate - datetime.date(year,month,day)).days 
timeSince = (datetime.date(year+1,month,day) - christmasDate).days

if timeLeft < 0:
    timeLeft = timeLeft + 365
    timeSince = timeSince - 365
    print 'from the date %s, there are %d days left \'til next christmas, and %d days since last christmas!' % (dateInput,timeLeft,timeSince)
else:
    print 'from the date %s, there are %d days left \'til next christmas, and %d days since last christmas!' % (dateInput,timeLeft,timeSince)
if timeLeft > timeSince:
    print 'the "closest" christmas was %s days ago' % timeSince
else:
    print 'the "closest" christmas is in %s days!' % timeLeft
