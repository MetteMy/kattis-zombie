n, m = input().split()

mlist = []
nlist = []
for i in n: 
    nlist.append(i)

for j in m: 
    mlist.append(j)
print(n)
print(nlist)

result = []
temp = 0

for i in range(len(nlist)):
    r = int(mlist[-1]) + int(nlist[-1]) + temp


    print(mlist[-1], nlist[-1])
    mlist.pop()
    nlist.pop()
    
    if r >= 10: 
        temp = 1
        r = r%10
    else:
        temp = 0
    result.append(r)
    
    print("r" , r)
    print("temp", temp)

if temp > 0:
    result.append(1)

result.reverse()
res = ""
for r in result:
    res += str(r)
print(res)


