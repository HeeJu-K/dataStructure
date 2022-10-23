# determine if an year is leap year

def leap_year(year): #leap year: divisible by 4 or 400, not divisible by 100(unless divisible by 400)
    if year%4 == 0 : # when divisible by 4, see if divisible by 100 or 400
        if year%100 == 0 and year%400 != 0: #if only divisible by 100 but not 400, is not a leap year
            return " is not a leap year"
        else : # if divisible by 400, is a leap year
            return " is a leap year"
    else:  #if not divisible by 4, is not a leap year
        return " is not a leap year"

input_year = int(input("Enter your year: ")) # input the year

if input_year<1582: # leap year rules were introduced by the Gregorian Calendar in 1582
    print("Please enter a valid year, 1582 onwards")
else: #print determined result
    print("Year "+str(input_year)+leap_year(input_year))