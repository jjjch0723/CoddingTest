# 쒸발 영어
treat_box = []
for i in range(3):
    treat_box.append(int(input()))

happy_score = (treat_box[0]*1)+(treat_box[1]*2)+(treat_box[2]*3)
if happy_score >= 10 :
    print("happy")
else :
    print("sad")