"""Addresses models.

- Personal Account
- Street
- Address
"""

from django.db import models


class PersonalAccount(models.Model):
    """Class that represent personal account model."""

    name = models.CharField(max_length=200, null=True)
    address = models.ForeignKey("Address", on_delete=models.PROTECT)

    is_cooperative_member = models.BooleanField(default=False)
    access_forbidden_since = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.address.street.short_name} {self.address.house_number}/{self.address.flat_number}"


class Street(models.Model):
    """Streets in the village."""

    short_name = models.CharField(max_length=5)
    full_name = models.CharField(max_length=100)
    KPP = models.ForeignKey("KPP", on_delete=models.PROTECT)

    def __str__(self):
        return self.full_name


class Address(models.Model):
    """Addresses model."""

    street = models.ForeignKey('Street', on_delete=models.PROTECT)
    house_number = models.SmallIntegerField()
    flat_number = models.SmallIntegerField()

    @property
    def name(self):
        return f"{self.street.short_name} {self.house_number}/{self.flat_number}"

    def __str__(self):
        return f"{self.street.short_name} {self.house_number}/{self.flat_number}"
