# You can tackle this challenge using the skills you've learned so far in the course. It might take you a moment to figure out a solution, but give it a try.

# Some concepts that you've learned about so far that might come in handy are looping, conditional statements, string methods, slicing, and indexing.

# As a stretch task you could adapt your solution so that it preserves capitalization of the original text, and that you can change the cipher to get a different encoding.

# Can you also write code to reverse the encryption?

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
encrypted = ""

for char in secret:
    #check for symbols and pass them through
    if char.lower() not in lowercase_letters:
        encrypted += char
    else:
        #find letter position in "lowercase_letters" variable
        foundPosition = lowercase_letters.find(char.lower())
        #find what letter is 7 spaces to that letters left
        newLetter = lowercase_letters[(foundPosition -7)]
        encrypted += newLetter
print(encrypted)


    


