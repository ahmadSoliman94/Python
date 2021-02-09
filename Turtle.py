import turtle
w = turtle.Screen()
w.bgcolor("black")
color = ["red","green","yellow","blue","cyan","orange","gray","lightgreen","magneta","indigo","purple"]

t = turtle.Turtle()
t.speed(1000)

for i in range(180):
     t.color(color[i%8])
     t.fd(i)
     t.left(250)
     t.circle(i)



turtle.done()