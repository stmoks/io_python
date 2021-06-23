#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Letters/starting_letter.txt') as letter:
    letter = letter.read()

with open('Input/Names/invited_names.txt') as names:
    names = names.readlines()

for name in names:
    stripped_name = name[:-1]
    new_letter = letter.replace('[name]',stripped_name)
    new_letter = new_letter.replace('Angela','Sechaba')
    with open(f'letter_for_{stripped_name}.txt','w') as output_letter:
        output_letter.write(new_letter)
    
    


  