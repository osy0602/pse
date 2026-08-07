class BMI:
    def calculate(self):
        height, weight = map(float, input("Enter your height(meter) and weight(kg): ").split())
        print("Your BMI: ", round((weight / height ** 2), 2), "%")

def main():
    bmi = BMI()
    bmi.calculate()

if __name__ == "__main__":
    main()
