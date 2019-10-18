# function
def count_words(s, n):
    # Create an empty dictionary
    d = dict()

    # Split the text into words  (string >> list)
    words = s.split(" ")
    print(words)
    # Iterate over each word in text
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

    p = list(d.items())
    p_s = sorted(p, key=lambda t: t[0])

    p_sortna = sorted(p_s, key=lambda t: t[1], reverse=True)

    res = p_sortna[:n]
    return res


# text
text = input("Enter a list element separated by space ")
n = int(input("Enter a number of top "))
#n = 3
# text = "cat bat mat cat bat cat"

print(count_words(text, n))
