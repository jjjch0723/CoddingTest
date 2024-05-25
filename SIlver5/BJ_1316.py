leng = int(input())
checker = leng

for i in range(leng):
    words = input()
    for j in range(len(words) - 1):
        if words[j] == words[j+1] :
            pass
        elif words[j] in words[j+1:]:
            checker -= 1
            break

print(checker)