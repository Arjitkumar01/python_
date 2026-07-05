# Q7.  Create a class Temperature with private __celsius.
#      Add:
#        set_celsius(value)   → sets value (raise error if < -273.15)
#        get_celsius()        → returns celsius
#        get_fahrenheit()     → returns converted value
#        get_kelvin()         → returns converted value

class Temperature:
    def __init__(self,celsius=0):
        self.__celsius=celsius
        
    def set_celsius(self,value):
        if value<-273.15:
            return "error"
        else:
            self.__celsius=value
    def get_celsius(self):
        return self.__celsius
    def get_fahrenheit(self):  
        return ((self.__celsius*9/5)+32)
    def get_kelvin(self):
        return (self.__celsius + 273.15 )
    
t1=Temperature()
t1.set_celsius(20)
print(t1.get_celsius())
print(t1.get_fahrenheit())
print(t1.get_kelvin())
