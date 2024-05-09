my_list=[]
while True:
    a=input()
    my_list.append(a)
    if a is 0:
        break
cnt=0
for i in range(1,len(my_list)):
    if my_list[i]>my_list[i-1]:
        cnt+=1
print(cnt)

