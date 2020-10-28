from django.db import models

HISTORY = (
    ('M' ,'Modern'),
    ('H' , 'Historic'),
    ('P' , 'Pre-Historic')
)

METALS = (
    ('G', 'GOLD'),
    ('S', 'SILVER'),
    ('B', 'BRONZE')
)

class Coincollector(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    moto = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Coin(models.Model):
    name = models.CharField(max_length=100)
    datefound = models.DateField()
    category = models.CharField(
        max_length=1,
        choices=HISTORY,
        default=HISTORY[0][0]
    )
    metal = models.CharField(
        max_length=1,
        choices=METALS,
        default=METALS[0][0]
    )

    coincollector = models.ForeignKey(Coincollector,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_category_display()} coin found on {self.datefound}'
    
    