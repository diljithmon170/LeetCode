prices=[1,2,3,4]
max_price=0
diff=0
for i in range(len(prices)):
    if prices[i]>max_price:
        max_price=prices[i]
        idx=i
for i in range(idx,len(prices)):
    t=abs(prices[idx]-prices[i])
    if t>diff:
        diff=t
print(diff)