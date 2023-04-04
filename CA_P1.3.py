"""
Chit Chat Application - Function:
How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words. """

a=input()
word_list=a.split()[:30]
output=" ".join(word_list)
print(output)