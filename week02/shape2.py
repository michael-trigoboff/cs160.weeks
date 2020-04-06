import turtle as t

# colors coded as strings using names from the Turtle Graphics Colors page
fillColor = 'yellow green'
lineColor = 'firebrick3'
bgColor = 'pale goldenrod'

# window
windowTitle = 'CS 160 - Shape 2'
windowWidth = 600
windowHeight = 600

# turtle speed names
turtleSpeeds = ['fastest', 'fast', 'normal', 'slow', 'slowest']

def setup(wnTitle, wnWidth, wnHeight, penX, penY, bgColor):
	# window properties
	t.title(wnTitle)
	t.bgcolor(bgColor)

	t.setup(wnWidth, wnHeight, 0, 0)	# window size, turtle initial position

	# set window coordinates of bottom-left corner to 0,0
	t.setworldcoordinates(0, 0, wnWidth, wnHeight)

	# pen properties (turtle starts out pointed horizontally to the right)
	t.speed(turtleSpeeds[4])

	# initial pen position
	t.penup()						# don't draw while positioning
	t.setpos(penX, penY)			# set pen position

setup(windowTitle, windowWidth, windowHeight, windowWidth / 2, windowHeight * 0.82, bgColor)

# set up shape
t.color(lineColor)					# set pen color
t.fillcolor(fillColor)
t.width(4)  						# set pen width
nVertices = 5
vertexAngle = 360 / nVertices
linelgth = 260

t.pendown()
t.begin_fill()

t.setheading(90)					# point straight up
t.right(90 + vertexAngle / 2)
for i in range(1, nVertices + 1):
	t.forward(linelgth)
	t.right(vertexAngle)

t.end_fill()

t.exitonclick()						# keep window open until mouse click
