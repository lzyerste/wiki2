def palindrome(s):  # string
    return s == s[::-1]


def palindrome1(s):  # sequence
    i = 0
    j = len(s) - 1
    while i <= j and s[i] == s[j]:
        i += 1
        j -= 1
    return True if i > j else False


def palindrome2(n):  # number
    return palindrome(str(n))


def palindrome3(n):  # number
    num_lst = list()
    while n >= 10:
        n, r = divmod(n, 10)
        num_lst.append(r)
    num_lst.append(n)
    return palindrome1(num_lst)


if __name__ == '__main__':
    import time
    import sys
    print(palindrome1("aba" * 1000))
    # sys.exit(0)

    s = "aba" * 1000

    t1 = time.time()
    for i in range(10 ** 0):
        palindrome(s)
    t2 = time.time()
    print(t2 - t1)

    t1 = time.time()
    for i in range(10 ** 0):
        palindrome1(s)
    t2 = time.time()
    print(t2 - t1)

    n = int("121" * 1000)
    t1 = time.time()
    for i in range(10 ** 1):
        palindrome2(n)
    t2 = time.time()
    print(t2 - t1)

    t1 = time.time()
    for i in range(10 ** 1):
        palindrome3(n)
    t2 = time.time()
    print(t2 - t1)
