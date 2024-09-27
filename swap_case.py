s=input()
ss=""
for i in range(len(s)):
    if s[i].isupper():
        ss+=s[i].lower()
    else:
        ss+=s[i].upper()
print(ss)
