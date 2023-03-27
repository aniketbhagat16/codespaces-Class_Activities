"""Problem - I 

sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink"
print(verse, "\n")

# split sentence into list of words
sentence_list =  # You will have to fill out the function 
print(sentence_list, '\n')

# convert list to set to get unique words
sentence_set = 
print(sentence_set, '\n')

# print the number of unique words
num_unique = 
print(num_unique, '\n')"""

sentence= "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink"
sl=sentence.split()
print("Verse= "," ".join(sl[:15]))
print("sentence_list= ",sl,"\n")

ss=set(sl)
print("sentence_set= ",ss,"\n")

print("num_unique: ",len(ss),"\n")