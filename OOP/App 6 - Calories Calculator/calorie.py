class Calorie:
    """
        Represent amount of calories calculates with
        BMR + 10*weight + 6.25*height + 5*age - 10*Temperature
    """
    
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
        
    def calculate(self):
        pass