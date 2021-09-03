# setting up for range
for i in range(1, 11):

    # if number is divisible by 3 and 5 print FizzBuzz
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')

    # if divisible by 3 print Fizz
    elif i % 3 == 0:
        print('Fizz')

    # if divisible by 5 print Buzz
    elif i % 5 == 0:
        print('Buzz')

    # other wise just print value.
    else:
        print(str(i))
