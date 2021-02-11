n = int(input("enter the number: "))

s = str(n)
m = len(s)
for i in range(m - 1, -1, -1):
    print(s[i], end="")
print()