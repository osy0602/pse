def main():
    numbers = list(map(float, input("Enter your working hours and pay rate: ").split()))

    print("Gross Pay: ", numbers[0] * numbers[1])

if __name__ == "__main__":
    main()