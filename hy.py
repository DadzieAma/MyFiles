def novowel():
    s = input("Enter a string: ")
    for i in s:
        if i.upper()== "I":
            return True
    return False
        
print(novowel())