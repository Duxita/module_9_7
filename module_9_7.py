def is_prime(func):
    def wrapper(a,b,c):
        res = func(a,b,c)
        print(res)
        if res >1:
            for i in range(2,(res//2)+1):
                if (res % i) == 0:
                    return 'Составное'
                else:
                    return 'Простое'
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
