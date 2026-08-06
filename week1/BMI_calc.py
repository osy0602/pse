def main():
    #input user height and weight
    height, weight = map(float, input("Enter your height(meter) and weight(kg): ").split())

    #if the user input is invalid, print error message
    if height <= 0 or weight <= 0:
        print("Enter valid height and weight")
        return

    # if the user input is in centimeters, convert it to meters
    elif height > 3:
        print("Height should be in meters, but... this time I can change it to meters for you😒")
        height = height / 100

    #calculate BMI to percentage round to 2 decimal places
    print("BMI: ", round((weight / height ** 2), 2), "%")

if __name__ == "__main__":
    main()