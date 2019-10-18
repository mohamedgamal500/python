stopwords = ['to', 'a', 'for', 'by', 'an',
             'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

sent_l = sent.split()

acro = ""
for word in sent_l:
    if(word not in stopwords):
        acro = acro+word[0]+word[1]+'. '


l = list(acro)  # convert to list

print(l)
l[-2:] = []
print(l)
print(acro)
acro = ("".join(l))
print(acro)
