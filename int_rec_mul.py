def multiply(x: int, y: int) -> int:
    '''
    takes two integer arguments of the same even length
    and return their products

    let a, b, c, d --> upper, lower halves of x, y respectively
    n is the length of x and y(assume they have equal lengths)
    xy = (10^n)ac + (10^(n/2))(ad + bc) + bd
    '''
    n = min(len(str(x)), len(str(y)))

    if n == 1:
        print('f')
        return x * y

    else:
        print('b')
        a, b = x // (10**(n // 2)), x % (10**(n//2))
        c, d = y // (10**(n // 2)), y % (10**(n//2))

        ac = multiply(a, c)
        ad = multiply(a, d)
        bc = multiply(b, c)
        bd = multiply(b, d)

        return 10**n * ac + 10**(n//2) * (ad + bc) + bd


x, y = map(int, input().split())
print(f"{x} * {y} = {multiply(x, y)}")
