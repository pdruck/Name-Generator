# opens a file that contains a list of either male or female names
def openFile(gender):
	names_in_file = []
	if(gender == 'M' or gender == 'MALE'):
		# opens a list of boys names contained in the cwd
		file = open('namesBoys.txt', 'r')
	elif(gender == 'F' or gender == 'FEMALE'):
		# opens a list of girls names contained in the cwd
		file = open('namesGirls.txt', 'r')
	for line in file:
		line = line.strip('\n')
		line = line.lower()
		names_in_file.append(line)
	file.close()
	return names_in_file

# gets input from the user and returns their chosen gender
def get_gender():
	while(True):
		gender = input('Male or Female: ')
		gender = gender.upper()
		if(gender != 'M' and gender != 'F' and gender != 'MALE' and gender != 'FEMALE'):
			print('Error: Please enter either (M)ale or (F)emale')
		else:
			return gender

# gets input from the user and returns their chosen minimum generated name length
def get_min_length():
	while(True):
		try:
			min_length = int(input('Min Name Length: '))
		except ValueError:
			print('Error: Please enter a number')
		else:
			return min_length

# gets input from the user and returns their chosen maximum generated name length
def get_max_length():
	while(True):
		try:
			max_length = int(input('Max Name Length: '))
		except ValueError:
			print('Error: Please enter a number')
			continue
		if(max_length < min_length):
			print('Error: Please enter a number greater than or equal to minimum name length')
		elif(max_length == 1 and min_length == 1):
			print('Error: Cannot generate a name with only 1 letter')
			sys.exit()
		else:
			return max_length

# gets input from the user and returns their chosen number of generated names
def get_num_names():
	while(True):
		try:
			num_names = int(input('Number of Names: '))
		except ValueError:
			print('Error: Please enter a number')
		else:
			return num_names	

# goes through the list of names in the file and processes each name 2 letters at a time
# returns a dictionary that holds those 2 letters and the letter that follows them
def create_rules(names_in_file):
	# creates an empty dictionary that contains the following ruleset
	# key = 2 consecutive characters in a name
	# value = the character that follows those 2 characters
	rules = {}
	for name in names_in_file:
		current_name = '__' + name + '__'
		start_index = 0
		end_index = 1
		while(True):
			# the 2 letters that are currently being processed
			processing = current_name[start_index:end_index+1]
			if(start_index != 0 and processing == '__'):
				break
			else:
				next_char = current_name[end_index+1]
				if(processing not in rules):
					rules[processing] = [next_char]
				else:
					rules[processing].append(next_char)
				start_index += 1
				end_index += 1
	return rules

# uses rules to randomly generate a name
# if the generated name is already contained in the list, generate a new name
def generate_name(names_in_file, rules, min_length, max_length):
	current_sequence = '__'
	generated_name = ''
	while(True):
		rand_index = random.randint(0, len(rules[current_sequence])-1)
		current_char = (rules[current_sequence])[rand_index]
		if(current_char == '_'):
			if(is_proper_length(generated_name, min_length, max_length) and is_unique(generated_name, names_in_file)):
				return generated_name
			else:
				#if the generated name is already in the list of names or not in between min and max length, try again
				current_sequence = '__'
				generated_name = ''
				continue
		else:
			# capitalize first letter of generated name
			if(current_sequence == '__'):
				generated_name += current_char.upper()
			else:
				generated_name += current_char

			current_sequence = current_sequence[1] + current_char

# checks if the generated name is already in the list of names
def is_unique(generated_name, name_list):
	for name in name_list:
		if(generated_name.lower() == name.lower()):
			return False
	return True

# checks if the generated name is between min and max length
def is_proper_length(generated_name, min_length, max_length):
	if(len(generated_name) >= min_length and len(generated_name) <= max_length):
		return True
	return False

def print_list(name_list):
	print()
	print('Here are the generated names:'),
	for generated_name in name_list:
		print(generated_name),
	print()

if __name__ == '__main__':
	import random
	import sys

	done = False
	while(not done):
		print('\n---Name Generator---\n')
		name_list = []

		# gets user input and stores it
		gender = get_gender()
		min_length = get_min_length()
		max_length = get_max_length()
		num_names = get_num_names()
		
		# creates a list of all the names in the file
		names_in_file = openFile(gender)
		rules = create_rules(names_in_file)

		# creates a list of names
		while(len(name_list) < num_names):
			name = generate_name(names_in_file, rules, min_length, max_length)
			# if generated name is not already in the list, add name to the list
			if(is_unique(name, name_list)):
				name_list.append(name)

		print_list(name_list)

		while(True):
			response = input('Again? Y or N: ')
			response = response.upper()
			if(response != 'Y' and response != 'N' and response != 'YES' and response != 'NO'):
				print('Error: Invalid response')
			else:
				if(response == 'N' or response == 'NO'):
					done = True
				break
