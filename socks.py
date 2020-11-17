socks = input("Enter set of numbers seperated by spaces ").strip().split()
pairs = 0
for element in set(socks):
    pairs += socks.count(element) // 2
print(f'The amount of pairs you have is {(pairs)}')