#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names = []
starting_letter = ""

with open("./Input/Names/invited_names.txt", mode="r") as file:
    invited_names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

for name in invited_names:
    new_letter = starting_letter.replace("[name]", name.strip().title())
    path = f"./Output\\ReadyToSend/{name.strip()}.txt"
    with open(path, mode="w") as file:
        file.write(new_letter)

