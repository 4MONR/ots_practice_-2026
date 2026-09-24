import turtle as t

t.speed(5)

state = "INIT"

x = 0
y = 0

while state != "STOP":

    if state == "INIT":
        t.setheading(90)
        state = "UP_1"

    elif state == "UP_1":
        t.forward(20)
        y += 1
        if y >= 2:
            t.setheading(0)
            state = "RIGHT_1"

    elif state == "RIGHT_1":
        t.forward(20)
        x += 1
        if x >= 2:
            t.setheading(270)
            state = "DOWN_1"

    elif state == "DOWN_1":
        t.forward(20)
        y -= 1
        if y <= -2:
            t.setheading(180)
            state = "LEFT_1"

    elif state == "LEFT_1":
        t.forward(20)
        x -= 1
        if x <= -2:
            t.setheading(90)
            state = "UP_2"

    elif state == "UP_2":
        t.forward(20)
        y += 1
        if y >= 4:
            t.setheading(0)
            state = "RIGHT_2"

    elif state == "RIGHT_2":
        t.forward(20)
        x += 1
        if x >= 4:
            t.setheading(270)
            state = "DOWN_2"

    elif state == "DOWN_2":
        t.forward(20)
        y -= 1
        if y <= -4:
            t.setheading(180)
            state = "LEFT_2"

    elif state == "LEFT_2":
        t.forward(20)
        x -= 1
        if x <= -4:
            t.setheading(90)
            state = "UP_3"

    elif state == "UP_3":
        t.forward(20)
        y += 1
        if y >= 4:
            t.setheading(90)
            state = "STOP"
t.done()
