#i = 8
#if(i%2 == 0):
    #print ("Even Number")
#else:
    #print ("Odd Number")
    
     
def get_age():
    age = int(input("Enter your age: "))
    print(age)
    if(age > 50):
        print("You are old")
    else:
        print("You are not old")
        
get_age()
