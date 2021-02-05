import random

# list of names that are in the drawing.
givers = [
    'Grandma',
    'Grandpa',
    
    'Tom',
    'Lori',
    
    'Kendall',
    'Alica',
    
    'Brianna',
    'Max MC',
    
    'Elijah',
    
    'Doug',
    'Staci',
    
    'Jennifer',
    'Brigham',
    
    'Rebecca',
    'Ben',
    
    'Shari',
    'Kirt',
    
    'Jake',
    'Kari',
    
    'Amanda',
    'Brett',
    
    'Steve',
    'Pam',
    
    'AJ',
    
    'Jayden(Boy)',
    
    'Jason',
    'Victora',
    
    'Kelsey',
    
    'Tyler',
    
    'Randy',
    'Kim',
    
    'Darrin',
    
    'Jessika',
    'Kyle',
    
    'Ryan',
    
    'Trevor',
    'Logan',
    
    'Sean',
    'Jasmine',
    
    'Lena',
    
    'Lisa',
    'Jacob',
    
    'Leanne'
    
    ]
# people that can't get each other
excludes = {
	'Grandma': 'Grandpa',
	'Tom': 'Lori',
	'Kendall': 'Alica',
    'Brianna' : 'Max MC',
    'Doug' : 'Staci',
    'Jennifer' : 'Brigham',
    'Rebecca' : 'Ben',
    'Shari' : 'Kirt',
    'Jake' : 'Kari',
    'Amanda' : 'Brett',
    'Steve' : 'Pam',
    'Jason' : 'Victora',
    'Randy' : 'Kim',
    'Jessika' : 'Kyle',
    'Trevor' : 'Logan',
    'Sean' : 'Jasmine',
    'Lisa' : 'Jacob'
}

def genSecretSanta():
	result = []
	restart = True

	while restart:
		restart = False
		receivers = givers[:]

		for i in range(len(givers)):
			giver = givers[i]
			# Pick a random reciever
			receiver = random.choice(receivers)

			# If we've got to the last giver and its the same as the reciever, restart the generation
			if (giver == receiver and i == (len(givers) - 1)):
				restart = True
				break
			else:
				# Ensure the giver and reciever are not the same, and they are not in the excludes list
				while (receiver == giver) or (receiver in excludes and giver == excludes[receiver]):
					receiver = random.choice(receivers)
				# Add result to array
				result.append(giver + ', ' + receiver)
				# Remove the reciever from the list
				receivers.remove(receiver)
	myFile = open('names.csv', 'w')
	myFile.write('Giver' + ', ' + 'Reciver' + '\n')
	for r in result:
		myFile.write(r + '\n')
	myFile.close()

def main():
	genSecretSanta()

if __name__ == '__main__':
	main()