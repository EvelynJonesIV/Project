import turtle, random
wn = turtle.Screen()
wn.bgcolor("black")
bob = turtle.Turtle()
lena = turtle.Turtle()

r = int(input("Enter a number of repeats. (Over 50 is recommended) "))
l = int(input("Enter a length "))
t = 0
colorset = int(input("Enter 1, 2, 3, 4, 5, or 6 for colors "))

if colorset == 0:
    wn.bgcolor("white")
    colors = ["black"]
    colorLena = ["purple"]
elif colorset == 1:
    colors  = ["red","green","blue","purple","yellow"]
    colorLena = ["pink", "orange", "maroon"]
elif colorset == 2:
    colors  = ["blue","purple"]
    colorLena = ["pink", "yellow"]
elif colorset == 3:
    colors  = ["red","blue"]
    colorLena = ["purple", "orange"]
elif colorset == 4:
    colors  = ["purple","yellow"]
    colorLena = ["red", "pink"]
elif colorset == 5:
    colors  = ["red", "green"]
    colorLena = ["maroon", "blue"]
elif colorset == 6:
    colors = ["white"]
    colorLena = ["white"]
else:
    colors = ["grey"]
    colorLena = ["grey"]

bob.speed(0)
bob.left(180)
while t < r:
    color = random.choice(colors)
    bob.color(color)
    bob.forward(l)
    bob.left(120)
    color = random.choice(colors)
    bob.color(color)
    bob.forward(l)
    bob.left(120)
    color = random.choice(colors)
    bob.color(color)
    bob.forward(l)
    bob.left(120)
    color = random.choice(colors)
    bob.color(color)
    bob.forward(l * t)
    bob.left(120)

    t = t + 1

t = 0
lena.speed(0)
while t < r:
    color = random.choice(colorLena)
    lena.color(color)
    lena.forward(l)
    lena.left(90)
    lena.forward(l)
    lena.left(90)
    l = l * 1.125
