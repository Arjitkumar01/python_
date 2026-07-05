# Q5.  Create a class Car with private __speed.
#      Add:
#        accelerate(amount)  → increases speed (max 200)
#        brake(amount)       → decreases speed (min 0)
#        get_speed()         → returns current speed
#      Speed should never go below 0 or above 200.

class Car:
    def __init__(self,speed=0):
        self.__speed=speed
        pass
    def accelerate(self,amount):
        if amount>0 and amount<200:
            self.__speed+=amount
        else:
            return "not possible"
    def brake(self,amount):
        if amount <=self.__speed:
            self.__speed-=amount
        else:
            return "not possible"
    def get_speed(self):
        return self.__speed
s1=Car()
print(s1.get_speed())
s1.accelerate(150)
print(s1.get_speed())
s1.brake(20)
print(s1.get_speed())
        
        