n = int(input())

pn = [0] * 10000001

for i in range (2, n+1) :
    pn[i] = pn[i-1] + 1
    
    if i % 2 == 0:
        pn[i] = min(pn[i], pn[i//2] + 1) 
    
    if i % 3 == 0 :
        pn[i] = min(pn[i], pn[i//3] + 1)

print(pn[n])