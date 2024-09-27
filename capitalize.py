s=input()
ss=""
ss+=s[0].upper()
for i in range(1,len(s)):
    if s[i]==' ':
        ss+=' '
        ss+=s[i+1].upper()
    else:
        ss+=s[i]

print(ss)


#answer
print(' '.join(word.capitalize() for word in s.split(' ')))