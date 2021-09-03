from functools import __cached__, lru_cache


@lru_cache(maxsize=5)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + (n - 2)


def main():
    for i in range(11):
        print(i, fib(i))
    print("done")


if __name__ == '__main__':
    main()
