w = input()
alph = 'abcdefghijklmnopqrstuvwxyz'
s_list = [w.find(c) for c in alph]
print(' '.join(map(str, s_list)))