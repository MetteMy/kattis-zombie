import time
start = time.time()

n, m = input().split()

mlist = []
nlist = []
for i in n: 
    nlist.append(i)

for j in m: 
    mlist.append(j)

def add(nlist,mlist, temp, result):
    
    if nlist == [] and mlist == []:
        return str(temp) if temp > 0 else ""
    
    
    a = int(nlist[-1]) if nlist else 0
    b = int(mlist[-1]) if mlist else 0
    
    r = 0
    for _ in range(a+b+temp):

        r +=1
    if r >= 10: 
        temp = 1
        r = r%10
    else:
        temp = 0
    
    for _ in range(10**7 * r): 
        pass
  
    return add(nlist[:-1], mlist[:-1], temp, result) + str(r)
  
print(add(nlist, mlist, 0, []))
# print(f"Kørselstid: {time.time() - start} sekunder")