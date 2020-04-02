# demonstrates Python functions

# returns nothing
def fn():
	print('fn called')

# returns 1 result
def add(x, y):
	print(f'adding {x} and {y}')
	return x + y

# returns 4 results
def arith(x, y):
	print(f'arith {x} and {y}')
	return x + y, x - y, x * y, x / y

# returns Boolean (True or False)
def gt(x, y):
	print(f'is {x} greater than {y}?')
	return x > y

fn()
print()					# skips a line

addRet = add(3, 4)
print(f'sum = {addRet}')
print()					# skips a line

if gt(3, 4):
	print('yes')
else:
	print('no')
print()					# skips a line
