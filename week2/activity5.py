class temperatureConverter:
    def __init__(self):
        self.temperature = ""

    def calculater(self):
        print("Welcome to Temperature Converter\n\n if you input start with 'F'\n we will convert it to Celsius\n and if you input start with 'C'\n we will convert it to Fahrenheit\n\n")
        self.temperature = input("Please enter the temperature you want to convert: ")

        #if user input is empty or not start with 'C' or 'F', print invalid input message
        if len(self.temperature) == 0:
            print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
        else:
            if self.temperature[0] == 'F': #only uppercase F or C is accepted
                #call the fahrenheit_to_celsius method and print the result
                converter = self.fahrenheit_to_celsius()
                print(self.temperature,"degrees Fahrenheit is converted to", f"{converter:.2f}", "degrees Celsius.")
            elif self.temperature[0] == 'C':
                #call the celsius_to_fahrenheit method and print the result
                converter = self.celsius_to_fahrenheit()
                print(self.temperature,"degrees Celsius is converted to", f"{converter:.2f}", "degrees Fahrenheit.")
            else:
                print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")

    def fahrenheit_to_celsius(self):
        return (float(self.temperature[1:]) - 32) * 5/9
    
    def celsius_to_fahrenheit(self):
        return (float(self.temperature[1:]) * 9/5) + 32

if __name__ == "__main__":
    #create an instance of the temperatureConverter class
    converter = temperatureConverter()

    #call the calculater method
    converter.calculater()