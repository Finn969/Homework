def largest(arg1):
    out = 0
    for i in arg1.split():
        s = sum(map(int,i))
        print (s)
        if s > out:
            out = s
    return out

print(largest("555 72 86 45 10"))