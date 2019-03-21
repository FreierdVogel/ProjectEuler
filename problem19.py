"""año = 0
if año%4==0 and  año%100!=0 or año%400==0:
    diasfeb = 29
else:
    diasfeb = 28

mes = {"jan":31, "feb":diasfeb, "mar":31, "abr":30, "may":31, "jun":30, "jul":31, "ago":31, "sep":30, "oct":31, "nov":30, "dec":31}

for i in range()"""
from itertools import count
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

year = 1901
monthcont = 0
for i in count(0):
    if not year%4:
        if not year%100:
            if not year%400:
                febdays = 29
            febdays = 28
        febdays=29

    monthdays = [31,febdays,31,30,31,30,31,31,30,31,30,31]
    print(dias[i%7])
