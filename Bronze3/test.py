#def sol(sentence, target):
sentence = "hello world this is a test"
target = "hello"

s = sentence.split()
answer = []
for char in s :
    if char == target :
        char = list(char)
        char[0] = char[0].upper()
        char = "".join(char)
    
    answer.append(char)
    print(answer)

answer = " ".join(answer)
print(answer)
    #return answer