def returnPosition(string, char):

    if char in string:
        newstring = string.replace(' ','')
        return newstring.index(char) + 1
    else:
        return -1

print(returnPosition("This is a Sentence","s"))