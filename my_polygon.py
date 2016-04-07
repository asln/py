from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


# t = turtle's name
# n = number of sides
# length = length of the sides
# r = radius



def polyline(t, n, length, angle):
    n = int(n)
    for i in range(n):
        fd(t, length)
        lt(t, angle)
    wait_for_user()
        

def square(t, length):
    polyline(t, 4, length, 90)
    

def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def circle(t, r):
    arc(t, r, 360)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360   # circumference * angle/360 = arc length
    n = (arc_length / 20) + 1  # the number of n is pre-determined by the coder
    step_length = arc_length / n  # finding the length of each n
    step_angle = float(angle) / n  # finding the angle of each side

    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

arc(bob, 50, 60)
    
    
        
