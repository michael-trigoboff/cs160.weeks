import random

print('Monty Python and the Holy Grail - The Bridge of Death')
print('https://www.youtube.com/watch?v=Wpx6XnankZ8')
print()				# print a blank line

print('Who would cross the Bridge of Death')
print('must answer me these questions three,')
print('ere the other side he see!')
print()				# print a blank line

# read name from the user
name =	input('What is your name? ')
print('Your name is ', name, '!', sep='')
print()				# print a blank line

# read quest from the user
quest =	input('What is your quest? ')
print('Your quest is to seek ', quest, '!', sep='')
print()				# print a blank line

# returns a random number between 0 and 1
randNum = random.random()

# choices
if randNum < .33:
    # read color from the user
    answer3 = input('What is your favorite color? ')
    print()			# print a blank line
    print('Right! Off you go!')
elif randNum > .67:
    # read capital from the user
    answer3 = input('What is the capital of Assyria? ')
    print()			# print a blank line
    print('Aaargh!')
else:
    # read airspeed from the user
    answer3 = input('What is the airspeed velocity of an unladen swallow? ')
    print()			# print a blank line
    print('Aaargh!')
print()				# print a blank line

# report user's answers
print('Your answers were:', name, ',', quest, ',', answer3)
print()				# print a blank line
