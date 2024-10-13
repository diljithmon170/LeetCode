def pal(word):
    if word[::-1]==word:
        if len(word)==4:
            return 5
        elif len(word)==5:
            return 10
        else:
            return 0
    else:
        return 0

srng="gfg iutiutiu iutiu fgf hjhjhjh uiiu uuiuu"
score=0
b=srng.split(" ")
for word in b:
    score+=pal(word)
print(score)