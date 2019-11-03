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
    # t is the parameter and t[0] is the returned value
    p_s = sorted(p, key=lambda t: t[0])
    # fetch the first tuples in the list and make the first elemnt of it as a key
    # sorted(iretable,key=fn)>>> pass each element of the list of tuples to the function parameter
    # then the function retun the value to the Key , the key value determine type of sorting(int,string,lenth..etc)
    p_sortna = sorted(p_s, key=lambda t: t[1], reverse=True)
    # fetch the first tuples in the list and make the second elemnt of it as a key
    res = p_sortna[:n]
    return res


# text
text = input("Enter a list element separated by space ")
n = int(input("Enter a number of top "))
#n = 3
# text = "cat bat mat cat bat cat"

print(count_words(text, n))
