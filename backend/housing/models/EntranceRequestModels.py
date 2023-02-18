from django.db import models


class EntrancePrices(models.Model):
    car_type = models.ForeignKey("CarType", on_delete=models.PROTECT)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.car_type.name} - {self.price}"


class EntranceRequest(models.Model):
    request_account = models.ForeignKey("PersonalAccount", on_delete=models.PROTECT, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    car = models.ForeignKey("Car", on_delete=models.PROTECT, null=True, blank=True)
    human = models.ForeignKey("Human", on_delete=models.PROTECT, null=True, blank=True)
    is_car = models.BooleanField(default=True)

    is_paid = models.BooleanField(default=False)
    # expires = date_created + 24

    note = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        if self.car:
            return f"{self.car.car_mark} - {self.car.car_number} | {str(self.request_account)}"
        return f"{self.human.name} | {str(self.request_account)}"
