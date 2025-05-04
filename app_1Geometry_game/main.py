import turtle


#create canvas instance
myturtle=turtle.Turtle()


#createing certain coordinates
myturtle.penup()
myturtle.goto(50,75)

myturtle.pendown()
myturtle.forward(100)  #here give argument as pixel
myturtle.left(90) #here give argument as degree
myturtle.forward(200)
myturtle.left(90) #here give argument as degree
myturtle.forward(100)
myturtle.left(90) #here give argument as degree
myturtle.forward(200)

turtle.done()