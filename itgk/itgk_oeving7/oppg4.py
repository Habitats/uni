#! /usr/bin/env python
# itgk oeving 7 - oppg4

# 1. jan 1900 = mandag

days = ['monday','tuesday','wedensday','thursday','friday','saturday','sunday']

def firstDayOfYear(x):
    # takes a year between 1900 and 2xxx
    dayCount = 0

    for i in range(1900,x):
        if isLeapYear(i) == True:
            dayCount += 366
        else:
            dayCount += 365
    return days[dayCount%7]

def isLeapYear(x):
    if x%4 == 0 and not x%100 == 0 or x%100 == 0 and x%400 == 0: # official way of checking for leap years 
        return True
    else:
        return False

def convertToDate(x,y):
    if isLeapYear(y):
        z = 29
    else:
        z = 28
    
    months = [31,z,31,30,31,30,31,31,30,31,30,31] 
    i = 0

    # this one's funny. it converts the day of year number into an actual date. 
    total = months[0]

    for i in range(0,12):
        if x <= total:
            x -= (total-months[i])
            return '%s.%s.%s' % (x+1,i+1,y)
        else:
            total += months[i+1]
   
# prompts the user to enter which weekdays the user intend to work, and return the result as a list with indexes from 'days'
def canWork(x):
    workDays = []
    for i in x.split(','):
        workDays.append(days.index(i))
    return workDays
        

# returns a list with all workdays for that year listed as indexes in "year". 0 = first day, 364 = last
def workDays(x,y):

    first = firstDayOfYear(x)

    # builds up the first days of the year as index values to the days (012 = mon tue wed)
    yearStr = '0123456'
    yearStr = yearStr[days.index(first):]

    while len(yearStr) <= 366:
        for i in days:
            yearStr += str(days.index(i))

    if isLeapYear(x):
        yearLen = 366
    else:
        yearLen = 365

    workDays = []

    # checks if the year index is a work day, if true add workday to list
    for i in range(0,len(yearStr[0:yearLen])):
        if int(yearStr[i]) in y:
            workDays.append(i)
    return workDays 


def workolator(year):
    return workDays(year,canWork(raw_input('enter the weekdays you indend to work in the format: day,day,day\n> ')))


year = input('enter a year\n> ')
for i in workolator(year):
    print convertToDate(i,year) # prints the converted date in a readable format



