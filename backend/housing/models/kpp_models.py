# KPP Data
from django.db import models


class EntranceType(models.Model):
    # represnts types like
    # калитка, шлагбаум
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Entrance(models.Model):
    # Represents specific entrances
    type = models.ForeignKey("EntranceType", on_delete=models.PROTECT)
    KPP = models.ForeignKey("KPP", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.KPP.name} {self.type}"


class KPP(models.Model):
    # Represents "КПП"
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"
