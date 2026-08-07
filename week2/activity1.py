class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def display(self):
        print("Your BMI: ", round((self.weight / self.height ** 2), 2), "%")

def main():
    height, weight = map(float, input("Enter your height(meter) and weight(kg): ").split())
    bmi = BMI(height, weight)
    bmi.display()

if __name__ == "__main__":
    main()
