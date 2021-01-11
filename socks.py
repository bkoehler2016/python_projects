socks = [2,3,3,4,4,4, 'a', 'a']
pairs = 0
for element in set(socks):
    pairs += socks.count(element) // 2
print(f'The amount of pairs you have is {(pairs)}') # should get 3 pairs