li=input().split()
low=li[0]
for i in li:
    if int(i)<int(low) and int(i)>0:
        low=i

print(low)