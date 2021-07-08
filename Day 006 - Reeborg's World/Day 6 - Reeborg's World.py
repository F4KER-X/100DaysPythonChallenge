def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():

    if right_is_clear() and not front_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
Day 006 - Reeborg's World
