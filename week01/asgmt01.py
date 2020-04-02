import turtle as t

# change this variable to be your own name
studentName = 'I. Forgot'

# colors coded as strings using names from the Turtle Graphics Colors page
dotColor = 'yellow green'
lineColor = 'firebrick3'

# window properties
t.title('CS 160 - Assignment 1 - ' + studentName)
t.bgcolor('pale goldenrod')

# set up window coordinates: 0,0 is bottom-left corner
width = 600
height = 600
t.setup(width, height, 0, 0)
t.setworldcoordinates(0, 0, width, height)

# pen properties
# (turtle starts out pointed horizontally to the right)
t.speed(0.51)					# set turtle speed to slowest
t.width(8)						# set pen width
t.color(lineColor)

# initial pen position
t.penup()						# don't draw while positioning
t.setpos(60, height / 2 - 60)	# set position

# draw uppercase letter M
t.pendown()
t.dot(20, dotColor)
t.left(90)
t.forward(120)
t.dot(20, dotColor)
t.right(135)
t.forward(60)
t.dot(20, dotColor)
t.left(90)
t.forward(60)
t.dot(20, dotColor)
t.right(135)
t.forward(120)
t.dot(20, dotColor)

t.exitonclick()					# keep window open until mouse click
