# 
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""       turtle-example-suite:

             tdemo_clock.py

Enhanced clock-program, showing date
and time
  ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from turtle import *
from datetime import datetime

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.15)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 125, 25)
    make_hand_shape("minute_hand",  130, 25)
    make_hand_shape("hour_hand", 90, 25)
    clockface(160)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray20", "gray80")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("blue1", "red1")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("blue3", "red3")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    #writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(85)

def wochentag(t):
    wochentag = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)

def tick():
    t = datetime.today()
    sekunde = t.second + t.microsecond*0.000001
    minute = t.minute + sekunde/60.0
    stunde = t.hour + minute/60.0
    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(wochentag(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.back(150)
        writer.write(datum(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(85)
        second_hand.setheading(6*sekunde)  # or here
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*stunde)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
"""     turtlegraphics-example-suite:

             tdemo_forest.py

Displays a 'forest' of 3 breadth-first-trees
similar to the one in tree.
For further remarks see tree.py

This example is a 'breadth-first'-rewrite of
a Logo program written by Erich Neuwirth. See
http://homepage.univie.ac.at/erich.neuwirth/
"""
from turtle import Turtle, colormode, tracer, mainloop
from random import randrange
from time import perf_counter as clock

def symRandom(n):
    return randrange(-n,n+1)

def randomize( branchlist, angledist, sizedist ):
    return [ (angle+symRandom(angledist),
              sizefactor*1.01**symRandom(sizedist))
                     for angle, sizefactor in branchlist ]

def randomfd( t, distance, parts, angledist ):
    for i in range(parts):
        t.left(symRandom(angledist))
        t.forward( (1.0 * distance)/parts )

def tree(tlist, size, level, widthfactor, branchlists, angledist=10, sizedist=5):
    # benutzt Liste von turtles und Liste von Zweiglisten,
    # fuer jede turtle eine!
    if level > 0:
        lst = []
        brs = []
        for t, branchlist in list(zip(tlist,branchlists)):
            t.pensize( size * widthfactor )
            t.pencolor( 255 - (180 - 11 * level + symRandom(15)),
                        180 - 11 * level + symRandom(15),
                        0 )
            t.pendown()
            randomfd(t, size, level, angledist )
            yield 1
            for angle, sizefactor in branchlist:
                t.left(angle)
                lst.append(t.clone())
                brs.append(randomize(branchlist, angledist, sizedist))
                t.right(angle)
        for x in tree(lst, size*sizefactor, level-1, widthfactor, brs,
                      angledist, sizedist):
            yield None


def start(t,x,y):
    colormode(255)
    t.reset()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.setpos(x,y)
    t.pendown()

def doit1(level, pen):
    pen.hideturtle()
    start(pen, 20, -208)
    t = tree( [pen], 80, level, 0.1, [[ (45,0.69), (0,0.65), (-45,0.71) ]] )
    return t

def doit2(level, pen):
    pen.hideturtle()
    start(pen, -135, -130)
    t = tree( [pen], 120, level, 0.1, [[ (45,0.69), (-45,0.71) ]] )
    return t

def doit3(level, pen):
    pen.hideturtle()
    start(pen, 190, -90)
    t = tree( [pen], 100, level, 0.1, [[ (45,0.7), (0,0.72), (-45,0.65) ]] )
    return t

# Hier 3 Baumgeneratoren:
def main():
    p = Turtle()
    p.ht()
    tracer(75,0)
    u = doit1(6, Turtle(undobuffersize=1))
    s = doit2(7, Turtle(undobuffersize=1))
    t = doit3(5, Turtle(undobuffersize=1))
    a = clock()
    while True:
        done = 0
        for b in u,s,t:
            try:
                b.__next__()
            except:
                done += 1
        if done == 3:
            break

    tracer(1,10)
    b = clock()
    return "runtime: %.2f sec." % (b-a)

if __name__ == '__main__':
    main()
    mainloop()


