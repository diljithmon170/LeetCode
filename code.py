# def hai(n):
#     if n[::-1]==n:
#         return True
#     return False

# n=input()
# print(hai(n))


def sum(a,n):
    for i in range(len(a)-1):
        for j in range(1,len(a)):
            if a[i]+a[j]==n:
                print([i,j])
a=[1,3,7,9,5]
n=12
sum(a,n)