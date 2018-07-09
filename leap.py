def get_age():
    age = int(input("Enter the year you were born: "))
    
    if(age%4) == 0:
        if(age%100) == 0:
            if(age%400) == 0:
                print("{0} is a leap year".format(age))
            else:
                print("{0} is not a leap year".format(age))
        else:
            print("{0} is a leap year".format(age))
    else:
        print("{0} is not a leap year".format(age))
        
get_age()