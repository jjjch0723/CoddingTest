a = input()
b = a.zfill(2)
index = 0
ori = b
while True:
    a_ = [int(char) for char in b]
    c = a_[0] + a_[1]
    b = b[-1] + str(c)[-1]
    index = index + 1
    if b == ori:
        break

print(index)
