a = [0,1,2,3,4,5,6,7,8,9]

b = [ x*2 for x in a if x <=5]
print(b)

b = []

for x in a:
    if x <= 5:
        b.append(x * 2)