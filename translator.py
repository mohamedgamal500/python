def translator(phrase):

    lenth = len(phrase)
    for w in range(lenth):
        if phrase[w].lower() in "aeiou":
            if phrase[w].isupper():
                phrase = phrase.replace(phrase[w], "G")
            if phrase[w].islower():
                phrase = phrase.replace(phrase[w], "g")
            print(phrase)
    print(phrase)


translator(input("please insert the phrase :  "))
