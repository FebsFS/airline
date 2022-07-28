from django.db import models

# Create your models here.


class flyings(models.Model):
    fr = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    wh = models.DateTimeField(auto_now_add=False)
    price = models.PositiveIntegerField()
    co = models.IntegerField()
    Company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.fr + ' - ' + self.to


class Company(models.Model):
    name = models.CharField(max_length=100, default=' ')
    text = models.TextField()

    def __str__(self):
        return self.name


