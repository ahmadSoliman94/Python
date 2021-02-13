#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t
t.bgcolor("black")
t.pensize(3)
def curve():
    for i in range (200):
        t.right(1)
        t.fd(1)
        t.speed(3)
t.speed(1)
t.color("red","red")
t.begin_fill()

t.speed(3)
t.left(140)
t.fd(112.65)
curve()

t.left(120)
curve()
t.fd(122.65)
t.end_fill()
t.hideturtle()
t.exitonclick()


# In[ ]:




