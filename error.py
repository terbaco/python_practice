a = 5
b = 5
c = 6
try:
    print(c/(a-b))
except ZeroDivisionError:
    print('Oh, no')