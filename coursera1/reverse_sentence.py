p_phrase = "was it a car or a cat I saw"
p_phrase_l = p_phrase.split()
r_phrase = " "


# reverse list of words
# suppose we have list of elements list = [1,2,3,4],
# list[0]=1, list[1]=2 and index -1 represents
# the last element list[-1]=4 ( equivalent to list[3]=4 )
# So, inputWords[-1::-1] here we have three arguments
# first is -1 that means start from last element
# second argument is empty that means move to end of list
# third arguments is difference of steps
p_phrase_l = p_phrase_l[-1::-1]

# now join words with space

r_phrase = r_phrase.join(p_phrase_l)

print(r_phrase)
