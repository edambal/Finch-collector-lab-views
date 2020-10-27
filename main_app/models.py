from django.db import models

# Create your models here.
class Coin:
    def __init__(self,name,metal,age,country):
        self.name=name
        self.metal=metal
        self.age=age
        self.country=country

mapleleaf = Coin('mapleleafy','gold',25,'USA')
    
coins = [
    Coin('maple leaf','gold',25,'Canada'),
    Coin('American Eagle','silver',35,'USA'),
    Coin('Valcambi Suisse','gold',15,'India'),
    Coin('Die Struck','bronze',115,'Greece')

]