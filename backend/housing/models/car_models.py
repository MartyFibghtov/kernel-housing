from django.db import models


class CarMark(models.Model):
    # Information table storing CarMarks
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarType(models.Model):
    # Store car types
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    # Change for longer foreign numbers
    car_number = models.CharField(max_length=9)
    owner = models.ForeignKey("PersonalAccount", on_delete=models.PROTECT, null=True, blank=True)
    car_mark = models.ForeignKey("CarMark", on_delete=models.PROTECT)
    car_type = models.ForeignKey("CarType", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.car_number} - {self.car_type} - {self.car_mark}"
