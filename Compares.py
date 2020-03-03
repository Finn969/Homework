def compares(string, int, char):
        if ((int-1) <= len(string))and(string.lower()[int-1] == char.lower()): return True

print(compares("The",2,'h'))