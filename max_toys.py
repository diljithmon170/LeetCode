prices=[1,4,5,3,2,1,6]
money=6
t=0
l1=[]
for i in range(len(prices)):
    j=i+1
    if j<=len(prices)-1:
        t=prices[i]+prices[j]
        if t<=money:
            l1.append(prices[i])
            l1.append(prices[j])
print(l1)

def getMaxToys(n, arr, money):
    L, H = 0, n - 1
    while L <= H:
        if sum(arr[L:H + 1]) <= money: break 
        else:
            if arr[L] > arr[H]:
                L += 1
            else:
                H -= 1
    return H - L + 2

n = int(input())
arr = list(map(int, input().split()))  # Read and split the input line
money = int(input())
print(getMaxToys(n, arr, money))