from django.db import models

class JSONModel(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=20)
    high = models.DecimalField(max_digits=20, decimal_places=3)
    low = models.DecimalField(max_digits=20, decimal_places=3)
    open = models.DecimalField(max_digits=20, decimal_places=3)
    close = models.DecimalField(max_digits=20, decimal_places=3)
    volume = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.trade_code} - {self.volume}"
    

    
    