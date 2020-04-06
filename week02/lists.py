# prints list in code-defined format
def printList(label, items):
	print(label + ': { ', end='')	# does not print newline at end of line
	for item in items:
		print(item + ' ', end='')	# does not print newline at end of line
	print('}')

print('demonstrates working with Python lists\n')

items = []							# start with empty list
print('empty list:', items)			# print list in Python default format
printList('empty list', items)
print()

items.append('def')					# append item to end of list
items.append('abc')					# append item to end of list
print('unsorted:', items)			# print list in Python default format
printList('unsorted', items)
print()

items.sort()						# sort list into alphabetic order
print('sorted:', items)				# print list in Python default format
printList('sorted', items)
print()

numbers = []
for i in range(1, 11):
	numbers.append(i)
first = numbers[0]
second = numbers[1]
last = numbers[-1]
listSlice = numbers[1:-2]

pass