T = int(input())

for _ in range(T):
    n = int(input())
    binary_value = bin(n)[2:]    
    positions = [i for i, bit in enumerate(reversed(binary_value)) if bit == '1']
    print(" ".join(map(str, positions)))
