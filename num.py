def int_to_roman (integer):
    parts = []
    for letter, value in TABLE:
        while value <= integer:
            integer -= value
            parts.append(letter)
    return ''.join(parts)

def rom_to_int(string):
    result = 0
    for letter, value in table:
        while string.startswith(letter):
            result += value
            string = string[len(pairs[0]):]
    return result       
