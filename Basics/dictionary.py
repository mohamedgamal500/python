def translator(phrase):
    dictionary = {
        "i": "ich",
        "am": "bin",
        "man": "mann",
        "good": "gut",
        "like": "mag",
        "cat": "katze"
    }
    output = ''
    for word in phrase:
        print(word, end=" ")
        output += dictionary.get(word, '!') + " "
    print("")
    return output


input_string = input("Enter a list element separated by space ")
phrase = input_string.split()
print(phrase)
print(translator(phrase))
