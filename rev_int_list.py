# my sol

x=1534236469
# s=str(x)
# r=""
# rv=s[::-1]
# l=list(rv)
# if len(l)>1:
#     while l[0]=="0":
#         l.pop(0)
# if l[-1]=="-":
#     l=[l[-1]] + l[:-1]
# for j in range(len(l)):
#     r+=l[j]
# x=int(r)
# print(x)


#solutio !

mod = 2**31  # Modulo for overflow checking
sign = -1 if x < 0 else 1
x *= sign
reversed_number = int(str(x)[::-1])
# Check for overflow
if reversed_number > mod - 1:
    print(0)
else:
    print(sign * reversed_number)