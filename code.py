def hai(n):
    if n[::-1]==n:
        return True
    return False

n=input()
print(hai(n))