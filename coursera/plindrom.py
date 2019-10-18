p_phrase = "was it a car or a cat I saw"
p_phrase_l = p_phrase.split()
r_phrase = " "
r_phrase_l = []
p_phrase_l = p_phrase_l[-1::-1]

for word in p_phrase_l:
    r_word = word[::-1]
    r_phrase_l.append(r_word)

r_phrase = r_phrase.join(r_phrase_l)

print(r_phrase)
