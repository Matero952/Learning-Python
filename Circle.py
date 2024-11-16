#Import math module.
import math
#Define the Circle class.
class Circle:
    #This is the init method, which is the constructor.
    #Automatically called when an object is created.
    def __init__(self, radius):
        #Self always gets passed in as an argument.
        #Then, we passed in the radius as a constructor.
        self.radius = radius
        #Initializes radius of a circle as an instance variable.
        self.circumference = 2 * math.pi * self.radius
        #Initializes circumference of a circle to
        #2 * pi * radius instance variable.
        self.areaOfACircle = self.solve_for_area()
        #Initializes area of a circle as the output of the function.

    #Defines a method to solve for the area of a circle.
    #Takes in self because it is taking in the instance variables of the class.
    def solve_for_area(self):
        area = math.pi * (self.radius ** 2)
        #Formula for the area of circle and exponent operator.
        return area
        #Function output
#Creates an instance of the class Circle and passes in the radius parameter.
my_circle = Circle(2)
#These are f strings, which are used to cleanly insert variables into strings.
#We use this instead of print("Circumference: " + str(circle.circumference))
print(f"Circumference: {my_circle.circumference}")
print(f"Area: {my_circle.areaOfACircle}")


