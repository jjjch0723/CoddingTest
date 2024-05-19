c_major = list(map(int, input().split()))

if c_major == sorted(c_major):
    print("ascending")
elif c_major == sorted(c_major, reverse=True) :
    print("descending")
else : 
    print("mixed")