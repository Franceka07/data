import turtle

'''
 Todo
    create two turtle elements cat and god 
    that will write
    messages on the screen


'''
# create window
window = turtle.Screen()

# create turtle obj
cat = turtle.Turtle()
dog = turtle.Turtle()


cat.color('green')
dog.color('blue')

# pull the pen up before we change position
cat.penup()
dog.penup()


# change position of cat and dog
cat.sety(-50)
dog.sety(50)

# hide the cat and dog, but keep the writing
cat.hideturtle()
dog.hideturtle()


cat.write('cat says milk', font = ('Courier',25))
dog.write('dog says wow', font = ('Courier',25))

turtle.mainloop()
