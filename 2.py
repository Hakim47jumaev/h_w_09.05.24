def factorial(a):
    res=1
    for i in range(1,a+1):
        res*=i
    return res
a=int(input())
sum=0
for i in range(1,a+1):
    sum+=factorial(i)

print(sum)