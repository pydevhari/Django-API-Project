from django.db import models

# Create your models here.

class Marks(models.Model):
    enroll = models.IntegerField()
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    obt = models.IntegerField()
    remark = models.CharField(max_length=20)
    total = models.IntegerField(default=10)
    result = models.CharField(max_length=5, default='')

    def __str__(self):
        return str(self.name)

class Addmision(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    mob = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)
