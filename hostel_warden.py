n=13
stud="Kkunjkhahorin"
st_pr=[]
st_cp=[]
st_ac=[]
for i in stud:
    # st_ac.append(ord(i))
    t=ord(i)
    for i in range(2,(t//2)+1):
        if t%i==0:
            flag=False
            break
        else:
            flag=True     
    if flag==True:
        st_pr.append(t)
    else:
        st_cp.append(t)
st_pr.sort()
st_cp.sort(reverse=True)
print(st_pr)
print(st_cp)
for i in st_pr:
    st_ac.append(i)
for i in st_cp:
    st_ac.append(i)
print(st_ac)
s=""
for i in st_ac:
    s+=chr(i)
print(s)
        

