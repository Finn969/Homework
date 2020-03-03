def zipped(s1,s2):
    outlist = [''*(len(s1)+len(s2))]
    l1 = list(s1)
    l2 = list(s2)
    l1 =  outlist[0::2]
    l2 = outlist[1::2]
    return ''.join(outlist)

print(zipped("Dog","Cat"))