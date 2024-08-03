# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

we = word[1:3]
see = word[-2]+word[-4]+word[-4]
tr = word[0]+word[-3]
trees = tr + see[::-1]

print(we+" "+see+" "+trees)