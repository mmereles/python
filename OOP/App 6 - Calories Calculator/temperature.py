class Temperature:
    """
    Represent a temperature vale extracted from the timeanddate.com/weather webpage
    """
    
    def __init__(self, country, city):
        self.country = country
        self.city = city
        
    def get(self):
        pass