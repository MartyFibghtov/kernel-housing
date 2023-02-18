from django.db import models


class InOutHistory(models.Model):
    is_entrance = models.BooleanField()

    datetime = models.DateTimeField(auto_now_add=True)

    # worker = models.ForeignKey(User)
    entrance = models.ForeignKey("Entrance", on_delete=models.PROTECT)

    # add photo when car / human cross for the first time
    def __str__(self) -> str:
        direction = "OUT"
        if self.is_entrance:
            direction = "IN "
        return f"{direction} - {self.datetime} - {self.entrance}"

    request = models.ForeignKey("EntranceRequest", null=True, on_delete=models.PROTECT)
    car = models.ForeignKey("Car", on_delete=models.PROTECT, null=True, blank=True)
    human = models.ForeignKey("Human", on_delete=models.PROTECT, null=True, blank=True)
