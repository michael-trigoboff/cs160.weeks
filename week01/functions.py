# demonstrates Python functions

# returns nothing
def fn(n):
	print(f'fn: called with {n}')

# returns 1 result
def add(x, y):
	sum = x + y
	print(f'add: adding {x} and {y}')
	print(f'add: returning {sum}')
	return sum

# returns Boolean (True or False)
def greaterThan(x, y):
	print(f'greaterThan: is {x} greater than {y}?')
	return x > y

fn(33)
print()					# skips a line

addRet = add(3, 4)
print(f'add function returned {addRet}')
print()					# skips a line

gt = greaterThan(3, 4)
if gt:
	print('yes')
else:
	print('no')
print()					# skips a line
