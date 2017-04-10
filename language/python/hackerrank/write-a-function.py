# https://www.hackerrank.com/challenges/write-a-function


def is_leap(year):
    #years=[2100,2400]
    #for i in range(len(years)):
    #    leap = (years[i]%4==0) and (years[i]%400==0 or years[i]%100!=0)
    #    print leap
    # Write your logic here
    leap = (year%4==0) and (year%400==0 or year%100!=0)
    return leap
