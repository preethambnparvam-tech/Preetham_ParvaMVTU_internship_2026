from datetime import datetime

print(f"Current Date & Time: {datetime.now()}")

print(f"Current Date: {datetime.today()}")

print(f"UTC Date and Time: {datetime.utcnow()}")

dob = datetime(2004, 7, 3, 14, 30, 45)
print(f"I was born on {dob}")

# strftime
# %A - Day in words full form (Monday)
# %a - Day in words short form (Mon)
# %d - Day in numerical form (15)
# %B - Month in words full form (March)
# %b - Month in words short form (Mar)
# %b - Month in words short form (3)
# %Y - Year in 4 digit (2026)
# %y - Year in 2 digit (26)
# %H - Hour in 24 hour format (14)
# %I - Hour in 12 hour format (2)
# %M - Minute (30)
# %S - Second (45)
# %p - AM/PM (PM)   
# %f - Microsecond (123456)
# %j - Day of the year (365)
# %U - Week number of the year (52) 
# %w - Weekday as a number (0-6, Sunday is 0)

print(f"Birth Month: {dob.strftime('%B')}")
print(f"Birth Month - short form: {dob.strftime('%b')}")
print(f"Birth Day: {dob.strftime('%A')}")
print(f"Birth Day - short form: {dob.strftime('%a')}")
print(f"Birth Year: {dob.strftime('%Y')}")
print(f"Birth Year - short form: {dob.strftime('%y')}") 
print(f"Birth Date: {dob.strftime('%d')}")
print(f"Birth Date in Day of the year: {dob.strftime('%j')}")
print(f"Birth Date in Week number of the year: {dob.strftime('%U')}") 
print(f"Birth Date in Hour: {dob.strftime('%H')}")
print(f"Birth Date in Minute: {dob.strftime('%M')}")   
print(f"Birth Date in Second: {dob.strftime('%S')}")
print(f"Birth Date in AM/PM: {dob.strftime('%p')}")
print(f"Birth Date in Microsecond: {dob.strftime('%f')}")   
print(f"My Birthday: {dob.strftime('%d-%b-%Y %H:%M:%S %p')}")

today = datetime.now()
print(f"Today is: {today.strftime('%A')}")
print(f"Today is: {today.strftime('%j')} day of the year")
print(f"Today is: {today.strftime('%U')} week of the year")

#Date Calculation
from datetime import datetime, timedelta,date
print(f"Yesterday was: {today + timedelta(days=-1)}")
print(f"Today is: {today}")
print(f"Tomorrow will be: {today + timedelta(days=1)}")

myAge = today.year - dob.year
print(f"My Age: {myAge}")