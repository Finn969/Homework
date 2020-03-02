def superBlock(s):
    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    max_count = 0
    for c in alphabet:
        count = s.count(c)
        if count > max_count:
            max_count = count
    return max_count
print(superBlock('hooplaaa'))