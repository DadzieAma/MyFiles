def even_only(lst):
    evens = 0
    for number in lst:
        if number%2 == 0:
            evens += number
    return evens

print (even_only([1,2,3,54]))