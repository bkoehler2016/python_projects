#function for word
def unique_count(word):
    # empty list to hold unique chars
  k=list()
  # for c in string if c not in list  list.append(c)
  for c in word:
    if c not in k:
      k.append(c)
  return len(k)

print(f'should be 9 answer:', unique_count('HeLlo WorLd')) # should be 9
print(f'should be 4 answer:', unique_count('hello')) # should be 4
print(f'should be 10 answer:', unique_count('gOoD MORninG')) # should be 10
print(f'should be 18 answer:', unique_count('Do Special Characters Count???')) # should be 18