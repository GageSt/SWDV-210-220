from dataclasses import dataclass

@dataclass
class Temp:
    fahrenheit: float = 32
    celsius: float = 0

    def getFahrenheit(self):
        return round(self.fahrenheit, 2)

    def setFahrenheit(self, fahrenheit):
        self.celsius = (fahrenheit - 32) * (5/9)
        self.fahrenheit = fahrenheit


    def getCelsius(self):
        return round(self.celsius, 2)
    
    def setCelsius(self, celsius):
        self.celsius = celsius
        self.fahrenheit = celsius * (9/5) + 32

# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    temp = Temp()
    for f in range(0, 212, 40):
        temp.setFahrenheit(f)
        print(temp.getFahrenheit(), "Fahrenheit equals", temp.getCelsius(), "Celsius")
    
    for c in range(0, 100, 20):
        temp.setCelsius(c)
        print(temp.getCelsius(), "Celsius equals", temp.getFahrenheit(), "Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()

