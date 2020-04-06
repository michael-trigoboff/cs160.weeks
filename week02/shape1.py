import turtle as t

# colors coded as strings using names from the Turtle Graphics Colors page
dotColor = 'yellow green'
lineColor = 'firebrick3'
bgColor = 'pale goldenrod'

# window
windowTitle = 'CS 160 - Shape 1'
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

setup(windowTitle, windowWidth, windowHeight, windowWidth / 2, windowHeight * 0.5, bgColor)

# set up shape
t.color(lineColor)					# set pen color
t.width(16)  						# set pen width
starPoints = 5
lineLgth = 200

t.pendown()
t.left(90)
for i in range(1, starPoints + 1):
	t.forward(lineLgth)
	t.back(lineLgth)
	t.right(360 / starPoints)

t.dot(256, dotColor)

t.exitonclick()						# keep window open until mouse click
