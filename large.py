inp_num=int(input())
list1=[]
for i in range(inp_num):
    x=input()
    list1.append(x)
first=list1[0]
second=list1[1]
list2=[]
for i in range(len(first)):
    if first[i]==second[i]:
        list2.append(first[i])
    else:
        break
res_str=''
for i in range(len(list2)):
    res_str+=list2[i]
new_list=[]
temp_str=''
if inp_num>2:
    for i in range(2,inp_num):
        temp=[]
        for i in range(len(list1[i])):
            if list1[i]==res_str[i]:
                temp.append()
            else:
                break
        if temp!=[]:
            temp_str=str(temp)
            new_list.append(temp_str)
new_list.append(res_str)
print(new_list[0])
