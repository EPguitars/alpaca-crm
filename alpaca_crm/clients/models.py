from django.db import models

# Create your models here.
class Customer(models.Model):
    PRIORITY_CHOICES = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )
    TYPE_CHOICES = (
        ('A', 'физлицо'),
        ('B', 'фирма'),
        ('C', 'исполнитель'),
    )

    name = models.CharField(max_length=255)
    tel_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    money_debt = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name