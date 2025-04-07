## A leap day (February 29) is added almost every four years to correct the calendar. 
## The year is a leap year if:
## 1. It's divisible by 4, unless:
## 2. It's NOT divisible by 100, unless:
## 3. It's divisible by 400 (then it's a leap year).
## Example: 2000 and 2400 are leap years; 1800, 1900, 2100, 2200, 2300, and 2500 are not.
def is_leap(year):
    #first you have to keep your self inside the leap condition
    #on each check point we say true or fals if all the conditions are thier then its true
    leap = False
    if year%4 == 0:
        leap = False
    #elif year%100 ==0: (ITS WORING MEN READ THE QUESTION AGAIN )
    elif year%100 !=0:
        leap = False
    elif year%400==0:
        leap =True
    # att this point if you dont add any thing the code would not give you shit you have to use return 
    # so we can print if its true or false men
    return leap
year = int(input())
print(is_leap(year))
# the elife we use it like when we want to compund conditions and not every condition sapperated to another

# i mean i did know how to write the code but still cant understand the logic to solve it
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap
    
year = int(input())
print(is_leap(year))
