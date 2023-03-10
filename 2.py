options = ['A', 'B', 'X']
result = []
for element1 in options:
    for element2 in options:
        if element1 != element2 or element1 == 'X':
            print(element1, element2)


