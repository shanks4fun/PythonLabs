# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = input("What is your Honest opinion of how I look? \n").lower()
turn = 0
updatedOpinion = ""
for char in opinion:
    if char.isalpha():
        turn += 1
        if turn % 2 == 0:
            updatedOpinion += char.capitalize()
        else:
            updatedOpinion += char.lower()

    else:
        updatedOpinion += char

print(updatedOpinion)