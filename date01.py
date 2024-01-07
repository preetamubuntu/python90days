# data module
from datetime import date
# print("today's date is " + date.today()) # throws error
print("today's date is " + str(date.today()))

parsecs = 11 # years
lightyears = parsecs * 3.26
print("11 parsecs is " + str(lightyears) + " lightyears") # you convert string in print function
