"""
Takes a hex color value as input and returns the corresponding
RGB value. Useful for HTML/CSS development.
"""

import string

def hex_to_rgb(value):
    line = value.strip(' ')
    line = line.lstrip('#')
    length = len(line)

    if length not in [3, 6]:
        return None

    chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    if not all(c in chars for c in line):
        return None

    if length == 3:
        line = ''.join([x*2 for x in line])

    result = []
    rgb = [line[i:i+2] for i in range(0, length, 2)]
    for x in rgb:
        result.append(str(int(x, 16)))
        
    return result

myhex = input('Enter hex color: ')
result = hex_to_rgb(myhex)

if result is not None:
    print('rgb(' + ', '.join(result) + ')')
else:
    print('Not a valid hex.')
