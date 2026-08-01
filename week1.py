def main():
    num = int(input("Enter a number: "))
    print("Fibonaci : ", fibonacci(num))
    print("Factorial : ", factorial(num))

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_number)
        return fib_sequence[-1]

def factorial(n):
    if n < 0:
        return "negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        fac_return = 1
        for i in range(2, n + 1):
            fac_return *= i
        return fac_return

if __name__ == "__main__":
    main()
