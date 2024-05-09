def sum(li):
    sun=0
    for i in li:
        sun+=int(i)
    return sun

li=[1,2,[3,4],5]
res=0
for i in li:
    if type(i) is list:
        res+=sum(i)
    else:
        res+=int(i)
print(res)