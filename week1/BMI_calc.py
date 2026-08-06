def main():
    #input user height and weight
    height, weight = map(float, input("Enter your height(meter) and weight(kg): ").split())

    #calculate BMI to percentage round to 2 decimal places
    print("BMI: ", round((weight / height ** 2), 2), "%")

if __name__ == "__main__":
    main()