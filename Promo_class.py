from datetime import datetime


class Promo:
    
    def __init__(self, name, expires):
        self.name = name
        self.expires =  expires

    @property
    def expires(self):
        return datetime.now() > self.expires
