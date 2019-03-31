# ---------------------------------------------------------------------
# Homework 6 -- A practice run for the final exam
# 3 Questions Total
# 100 Possible Points
# ---------------------------------------------------------------------

# 1) A clerk works in a store where the cost of each item
#    is a positive integer number of dollars.
#    So, for example, something might cost $21, but nothing costs $9.99.
#    In order to make change a clerk has an unbounded number of bills
#    in each of the following denominations: $1, $2, $5, $10, and $20.

# Write a program that takes two arguments: the cost of an item and the amount paid,
# and prints how to make change using the smallest possible number of bills.

# (20 Points)
# October 20. PK - a list of the denominations of available bills is also being passed to the
# function make_change. This will allow the user to pass a list of available denominations 
# to the function in case the clerk runs out of any types of bills.

def make_change(cost_of_item, amount_paid, denominations):

	""" A function to make change given the cost of an item, the amount paid and the denomination
	of bills that are in the cash register"""

	def data_quality_check(denominations, **kwargs):
		complete = True	
		
		for key, value in kwargs.items():
			if not isinstance(value, int):
				complete = False
				print('The {} is not an integer'.format(key))
			else:
				if value < 1:
					complete = False
					print('The {} is less than $1'.format(key))
		
		denom = list(set(denominations)) # get out any duplicates
		if not all(isinstance(x, int) for x in denom):
			complete = False
			print('At least one of the elements in the list is not an integer')
		if any(i < 1 for i in denom):
			complete = False
			print('At least one of the elements in the list is less than 1')
		if complete:
			denominations = sorted(denom, reverse=True) # sort list in reverse order
		return complete, denominations


	def amount_of_change(cost_of_item, amount_paid):
		print('Cost of the item is ${}'.format(cost_of_item))
		print('Amount paid is ${}'.format(amount_paid))
		return amount_paid - cost_of_item


	def denomination_of_bills(change, denominations):
		bills_to_return = []
		while change > 0:
			# set start = 0. Then change it to the count value every time a bill is chosen
			# so that the next loop does not start at the beginning of the list. This shortens
			# each succesive loop.
			start = 0
			for count, bill in enumerate(denominations, start):
				if bill <= change:
					bills_to_return.append(bill)
					change -= bill
					start = count
					break
		return bills_to_return
	
	##### Start the code #####
	## put items into a dictionary so that I can experiment with passing kwargs.
	
	info_dict = {'cost of item': cost_of_item, 'amount paid' : amount_paid}
	complete, denominations = data_quality_check(denominations, **info_dict)
	if not complete:
		return

	change = amount_of_change(cost_of_item, amount_paid)
	if change < 0:
		print("You haven't paid enough for the item.")
	elif change == 0:
		print('You paid the exact amount and get no change')
	else:
		print('The change is ${}'.format(change))
		bills = denomination_of_bills(change, denominations)
		if len(bills) == 1:
			print('The denomination of the change is ${}'.format(''.join(str(x) for x in bills)))
		else:
			print('The denominations of the change are ${}'.format(', $'.join(str(x) for x in bills)))



if __name__ == '__main__':
	print('Question 1')
	# Test 1 - this will fail
	cost_of_item = 0
	amount_paid = 'q'
	denominations = [5, 0, 1, 2, 'x', 10, 20, 50]
	make_change(cost_of_item, amount_paid, denominations)
	# Test 2 - this will pass
	print()
	cost_of_item = 8
	amount_paid = 50
	denominations = [5, 1, 2, 5, 10, 20, 50]
	make_change(cost_of_item, amount_paid, denominations)



# 2) Write a program that takes a string of words separated by spaces
#    (assume no punctuation or capitalization), together with a ”target” word,
#    and shows the index position of the target word in a list of the words.

#    Use the split() method to split the words from a string into a list.
#    split() method DOCS: https://docs.python.org/3/library/stdtypes.html#str.split


# For example, if the string is:
# 'we dont need no education we dont need no thought control no we dont'
# and the target is the word 'dont'
# then your program should return the list: [1, 6, 13].
# Your program should return False if the target word doesn’t appear in the string.

# (20 Points)
def split_words (sample_data, target_word):
	
	def create_string(sample_data):
		return (sample_data.split())

	def create_list(new_data, target_word):
		output_list = []
		for count, item in enumerate(new_data):
			if item == target_word:
				output_list.append(count)
		return output_list


	new_data = create_string(sample_data)
	output_list = create_list(new_data, target_word)
	print('The output list is {}'.format(output_list))


if __name__ == '__main__':
	print('\nQuestion 2')
	sample_data = 'we dont need no education we dont need no thought control no we dont'
	target_word = 'dont'
	split_words(sample_data, target_word)


# 3) Write a class called Employee.
# 3a) The __init__() method should take in:
#     a first name, a last name, and an annual salary,
#     and store each of these as attributes.
# 3b) Write a method called give_raise() that adds $5000 to
#     the annual salary by default but also accepts a different raise amount.
# 3c) Use your class object to create an Employee with your name.
#     And give yourself a raise!

# (60 points)
class Employee():

	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary
		self.increase = 0

	def give_raise(self, increase = 5000):
		self.increase = increase
		print("{} {}'s annual salary is ${:,.2f}".format(self.first_name, self.last_name, self.annual_salary))
		self.annual_salary += self.increase
		print("{} {}'s annual salary after the raise is ${:,.2f}".format(self.first_name, self.last_name, self.annual_salary))

print('\nQuestion 3')
# No raise is passed - use the default
my_comp = Employee('Peter', 'Koppelman', 100000)
my_comp.give_raise()
print()
# Make the raise $10,000 - override the default
my_comp2 = Employee('Peter', 'Koppelman', 100000)
my_comp2.give_raise(10000)

