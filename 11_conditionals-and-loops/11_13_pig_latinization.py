# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay

#read through word until you hit a space
#save word to variable
#edit word by taking first letter and moving it to the end and then add ay to it
#save that word with a space to a new variable

story = '''You would never guess what can happen when you jump into a seemingly shallow puddle at night time!
It turns out that it is not a puddle rather than a giant hole which brings you to a new world on the other side of the light water. Now you are left stunning and don't know what to do.
So you decide to call Whoolio who lives in Never Never land.
You can't believe your eyes. There are magical creatures of all shapes and sizes in all directions!
You tried to walk, but your body was not listening to you and it was very difficult to make a step
So you reached out your arm as far as it would go to see if you could touch a creature.
Just as you are about to touch one of the creatures the world around you suddenly shatters like a glass pane.
And that's when you realise that the world you've been living in has been made of marshmallows all along
That's the moment when you take your first bite into the soft and sweet world around you.
It tastes like... To your surprise, what should've been a soft sweet bite of marshmallow turned out to sting 
with ghost pepper like spiciness. You would never guess what can happen when you jump into a seemingly shallow puddle at night time!
It turns out that it is not a puddle rather than a giant hole which brings you to a new world on the other side of the light water. Now you are left stunning and don't know what to do.
'''
newStory = ""
word = ""
for char in story:
    if char == " ":
        newStory += word[1:] + word[0] + "ay "
        word = ""
    else:
        word += char

word = ""

for char in story[::-1]:
    if char == " ":
        word = word[::-1]
        newStory += word[1:] + word[0] + "ay"
        break
    else:
        word += char

print(newStory)