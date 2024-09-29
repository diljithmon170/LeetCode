n=6
powers=[9,3,1,2,4,2]
powers.sort(reverse=True)
dup, sum1, ans = 0, 0, 0
s=sum(powers)
for i in powers:
    dup += i
    sum1 = s - dup
    ans += 1
    if sum1 < dup:
        break
print(ans)
        





# for i in range(len(powers)-1):
#     for j in range(1,len(powers)):
#         ans=0
#         pow_sum=powers[i]+powers[j]
#         temp_sum=0
#         for k in range(len(powers)):
#             if not k==i==j:
#                 temp_sum=powers[k]
#         if temp_sum<pow_sum:
#             if temp_sum<ans


        # print(pow_sum)

