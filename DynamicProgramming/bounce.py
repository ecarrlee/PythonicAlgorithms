def stop(track, pos, start_speed):
    max_speed = len(track)-1
    solutions = {}
    for posistion in range(len(track)):
        if track[posistion]:
            solutions[posistion] = set([0])
            
    for posistion in reversed(range(pos, len(track))):
        if not track[posistion]:
            continue
        for speed in range(1,max_speed):
            for adjusted_speed in [speed+1,speed,speed-1]:
                new_posistion = posistion + adjusted_speed
                if new_posistion in solutions:
                    if adjusted_speed in solutions[new_posistion]:
                        solutions[posistion].add(speed)

    print(solutions[pos])
    return start_speed in solutions[pos]

print(stop([False,True,True,True,False],1,3))
