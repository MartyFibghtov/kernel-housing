from housing.models import kpp_models, contacts_models, car_models
from housing.models import address_models


# Create KPP
kpp1 = KPPmodels.KPP(name="КПП 1")
kpp2 = KPPmodels.KPP(name="КПП 2")

kpp1.save()
kpp2.save()

# Create entrance types
HumanType = KPPmodels.EntranceType(name="Калитка")
CarType = KPPmodels.EntranceType(name="Шлагбаум")

HumanType.save()
CarType.save()


# Create entrances
entrance1 = KPPmodels.Entrance(type=HumanType, KPP=kpp1)
entrance2 = KPPmodels.Entrance(type=HumanType, KPP=kpp2)
entrance3 = KPPmodels.Entrance(type=CarType, KPP=kpp1)
entrance4 = KPPmodels.Entrance(type=CarType, KPP=kpp2)

entrance1.save()
entrance2.save()
entrance3.save()
entrance4.save()


# Create streets
Lesnaya = AddressModels.Street(short_name='Л', full_name='Лесная', KPP=kpp1)
Youjnaya = AddressModels.Street(short_name='Ю', full_name='Южная', KPP=kpp1)
Zvesdnaya = AddressModels.Street(short_name='З', full_name='Звездная', KPP=kpp2)
SevTup = AddressModels.Street(short_name='СТ', full_name='Северный тупик', KPP=kpp2)

Lesnaya.save()
Youjnaya.save()
Zvesdnaya.save()
SevTup.save()

# Generate addresses
addresses_file_path = './data/addresses.csv'


import csv
import os

print(os.getcwd())
if os.path.exists(addresses_file_path):
    with open(addresses_file_path) as csvfile:
        reader = csv.reader(csvfile)
        addresses = [row for row in reader]
else:
    raise ValueError("File not found")
for address in addresses:
    print(address)
    street = AddressModels.Street.objects.filter(full_name=address[0]).first()
    if not street:
        street = SevTup
    address_model = AddressModels.Address(street=street, house_number=int(address[1]), flat_number=int(address[2]))
    address_model.save()



timur_nurmatov = AddressModels.PersonalAccount(
    name="Timur Nurmatov",
    address=AddressModels.Address.objects.filter(house_number=34, flat_number=8).first(),
    is_cooperative_member = True,
)
# Sample personal account
timur_nurmatov.save()


phone = ContactsModels.PhoneNumber(number='+79266263455', owner=timur_nurmatov)
phone.save()

email = ContactsModels.Email(email='tnk@gmail.com', owner=timur_nurmatov)
email.save()

tg_link = ContactsModels.TgLink(tg_link='@tnk', owner=timur_nurmatov)
tg_link.save()




# Create cars
car_marks = [
    "Lada",
    "Kia",
    "Hyundai",
    "Renault",
    "Skoda",
    "Volkswagen",
    "Toyota",
    "Nissan",
    "Ford",
    "Chevrolet"
]

for car_mark in car_marks:
    car_mark_model = CarModels.CarMark(name=car_mark)
    car_mark_model.save()


car_types = [
    'Грузовик',
    'Легковая',
    'Мотоцикл',
]


for car_type in car_types:
    car_type_model = CarModels.CarType(name=car_type)
    car_type_model.save()



# Sample car
car = CarModels.Car(
    car_number='a777aa149',
    owner=timur_nurmatov,
    car_type=CarModels.CarType.objects.filter(name='Легковая').first(),
    car_mark=CarModels.CarMark.objects.all().first()
)


