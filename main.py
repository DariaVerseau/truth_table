for x in range(2):
    for y in range(2):
        for z in range(2):
                r = bool((x + y) + (z or (not x)))
                if r == True:
                    r = 1
                else:
                    r = 0
                print(x, y, z, r)
