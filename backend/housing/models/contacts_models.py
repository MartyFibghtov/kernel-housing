from django.db import models


class PhoneNumber(models.Model):
    number = models.CharField(max_length=12)
    owner = models.ForeignKey("PersonalAccount", on_delete=models.PROTECT)

    def __str__(self):
        return self.number


class Email(models.Model):
    email = models.CharField(max_length=100)
    owner = models.ForeignKey("PersonalAccount", on_delete=models.PROTECT)

    def __str__(self):
        return self.email


class TgLink(models.Model):
    tg_link = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey("PersonalAccount", on_delete=models.PROTECT)

    def __str__(self):
        return self.tg_link
