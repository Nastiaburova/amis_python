a = float(input("Enter number: "))
n = int(input("Enter power of number:"))
def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        result = a * power(a, n - 1)
        return result

print(power(a, n))
