words_len = int(input())
words = []
for i in range(0, words_len):
    words.append(input())

words = list(set(words))
#튜플로 단어의 알파벳수와 단어를 저장
words.sort(key=lambda word: (len(word), word))

for i in words:
    print(i)