# implement an algorithm to determine if a string has all unique characters
# what if we can't use an additional data structure?

# data structure solution
def is_unique(string):
	ds = set()
	print "Checking uniqueness of string " + string

	for i in range(0, len(string)):
		ds.add(string[i])

	if len(ds) is len(string):
		print "True\n"
		return True

	print "length of set doesn't match length of string. Returning False.\n"
	return False


is_unique("hello")
is_unique("quickbrawnedfox")

def no_ds_isUnique(string):
	test_dict = {}
	is_unique = True

	for c in string:
		if(not test_dict.get(c, False)):
			test_dict[c] = c
		else:
			is_unique = False
			break
	if is_unique:
		return "String is unique"
	else:
		return "String is not unique"

print(no_ds_isUnique("hello"))
print(no_ds_isUnique("quickbrawnedfox"))
print(no_ds_isUnique("123567890asdf"))
print(no_ds_isUnique("12f3567890asdf"))

# not really a sort, just a modified form of
# left (i) pointer, right (j) pointer, traverse remainder of list with j
# and compare j value to i
# if duplicate, increment a counter
# when done, if the counter > 1, return True
def no_ds_sortUnique(string):
	for i in range(0, len(string)):

		charinput = string[i]
		count = 0

		for j in range(i, len(string)):
			if charinput == string[j]:
				count += 1

		if count > 1:
			print "Count > 1; returning False"
			return False

	print "Count = 0; returning True"
	return True

print(no_ds_sortUnique("hello"))
print(no_ds_sortUnique("quickbrawnedfox"))
print(no_ds_sortUnique("123567890asdf"))
print(no_ds_sortUnique("12f3567890asdf"))