import turtle as t

t.speed(5)

state = "INIT"

x = 0
y = 0

while state != "STOP":

    if state == "INIT":
        t.setheading(270)
        state = "DOWN_1"

    elif state == "DOWN_1":
        t.forward(20)
        y -= 1
        if y <= -8:
            t.setheading(0)
            state = "RIGHT_1"

    elif state == "RIGHT_1":
        t.forward(20)
        x += 1
        if x >= 8:
            t.setheading(90)
            state = "UP_1"

    elif state == "UP_1":
        t.forward(20)
        y += 1
        if y >= 0:
            t.setheading(180)
            state = "LEFT_1"

    elif state == "LEFT_1":
        t.forward(20)
        x -= 1
        if x <= 1:
            t.setheading(270)
            state = "DOWN_2"

    elif state == "DOWN_2":
        t.forward(20)
        y -= 1
        if y <= -7:
            t.setheading(0)
            state = "RIGHT_2"

    elif state == "RIGHT_2":
        t.forward(20)
        x += 1
        if x >= 7:
            t.setheading(90)
            state = "UP_2"

    elif state == "UP_2":
        t.forward(20)
        y += 1
        if y >= -1:
            t.setheading(180)
            state = "LEFT_2"

    elif state == "LEFT_2":
        t.forward(20)
        x -= 1
        if x <= 2:
            t.setheading(270)
            state = "DOWN_3"

    elif state == "DOWN_3":
        t.forward(20)
        y -= 1
        if y <= -6:
            t.setheading(0)
            state = "RIGHT_3"

    elif state == "RIGHT_3":
        t.forward(20)
        x += 1
        if x >= 6:
            t.setheading(90)
            state = "UP_3"

    elif state == "UP_3":
        t.forward(20)
        y += 1
        if y >= -2:
            t.setheading(180)
            state = "LEFT_3"

    elif state == "LEFT_3":
        t.forward(20)
        x -= 1
        if x <= 3:
            t.setheading(270)
            state = "DOWN_4"

    elif state == "DOWN_4":
        t.forward(20)
        y -= 1
        if y <= -5:
            t.setheading(0)
            state = "RIGHT_4"

    elif state == "RIGHT_4":
        t.forward(20)
        x += 1
        if x >= 5:
            t.setheading(90)
            state = "UP_4"

    elif state == "UP_4":
        t.forward(20)
        y += 1
        if y >= -3:
            t.setheading(180)
            state = "LEFT_4"

    elif state == "LEFT_4":
        t.forward(20)
        x -= 1
        if x <= 4:
            t.setheading(270)
            state = "DOWN_5"

    elif state == "DOWN_5":
        t.forward(20)
        y -= 1
        if y <= -4:
            state = "STOP"

t.done()
