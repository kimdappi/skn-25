import sys
list_check=[]
n = int(input())
for _ in range(n):
    data= input()
    name,check=data.split()
    if check=='enter':
        list_check[name]=1
    else:
        del list_check[name]
list_check.sort(reverse=True)

for name, _  in sorted(list_check.items(),key=lambda x : x[0],reverse=True):
    print(name)