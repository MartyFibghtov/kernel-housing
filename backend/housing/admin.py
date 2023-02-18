from django.contrib import admin

# Register your models here.
from django.contrib import admin
from housing.models.AddressModels import *
from housing.models.CarModels import *
from housing.models.ContactsModels import *
from housing.models.EntranceRequestModels import *
from housing.models.InOutHistoryModels import *
from housing.models.KPPmodels import *
from housing.models.VisitorModels import *

admin.site.register(PersonalAccount)
admin.site.register(Street)
admin.site.register(Address)


admin.site.register(CarMark)
admin.site.register(CarType)
admin.site.register(Car)


admin.site.register(PhoneNumber)
admin.site.register(Email)
admin.site.register(TgLink)


admin.site.register(EntrancePrices)
admin.site.register(EntranceRequest)

admin.site.register(InOutHistory)

admin.site.register(EntranceType)
admin.site.register(Entrance)
admin.site.register(KPP)

admin.site.register(Human)
