from django.contrib import admin

# Register your models here.
from django.contrib import admin
from housing.models.address_models import *
from housing.models.car_models import *
from housing.models.contacts_models import *
from housing.models.entrance_request_models import *
from housing.models.in_out_history_models import *
from housing.models.kpp_models import *
from housing.models.visitor_models import *

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
