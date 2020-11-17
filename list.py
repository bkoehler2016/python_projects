a = [44, 20, 129, 0]
a.insert(0, 999)
a.append(9999)

a[1]


for num in a:
    print (num)

for i, v in enumerate(a):
    print(f"{i}: {v}")
