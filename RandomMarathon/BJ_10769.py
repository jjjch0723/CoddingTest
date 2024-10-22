kakakotalk = input().strip()

happy_count = kakakotalk.count(":-)")
sad_count = kakakotalk.count(":-(")

if happy_count == 0 and sad_count == 0:
    print("none")
elif happy_count == sad_count:
    print("unsure")
elif happy_count > sad_count:
    print("happy")
else:
    print("sad")