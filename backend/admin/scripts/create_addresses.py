from housing.models import kpp_models, contacts_models, car_models
from housing.models import address_models
from housing.models import contacts_models

# Create KPP
kpp1 = kpp_models.KPP(name="КПП 1")
kpp2 = kpp_models.KPP(name="КПП 2")

kpp1.save()
kpp2.save()

# Create entrance types
HumanType = kpp_models.EntranceType(name="Калитка")
CarType = kpp_models.EntranceType(name="Шлагбаум")

HumanType.save()
CarType.save()


# Create entrances
entrance1 = kpp_models.Entrance(type=HumanType, KPP=kpp1)
entrance2 = kpp_models.Entrance(type=HumanType, KPP=kpp2)
entrance3 = kpp_models.Entrance(type=CarType, KPP=kpp1)
entrance4 = kpp_models.Entrance(type=CarType, KPP=kpp2)

entrance1.save()
entrance2.save()
entrance3.save()
entrance4.save()


# Create streets
Lesnaya = address_models.Street(short_name='Л', full_name='Лесная', KPP=kpp1)
Youjnaya = address_models.Street(short_name='Ю', full_name='Южная', KPP=kpp1)
Zvesdnaya = address_models.Street(short_name='З', full_name='Звездная', KPP=kpp2)
SevTup = address_models.Street(short_name='СТ', full_name='Северный тупик', KPP=kpp2)

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
    street = address_models.Street.objects.filter(full_name=address[0]).first()
    if not street:
        street = SevTup
    address_model = address_models.Address(street=street, house_number=int(address[1]), flat_number=int(address[2]))
    address_model.save()



timur_nurmatov = address_models.PersonalAccount(
    name="Timur Nurmatov",
    address=address_models.Address.objects.filter(house_number=34, flat_number=8).first(),
    is_cooperative_member = True,
)
# Sample personal account
timur_nurmatov.save()


phone = contacts_models.PhoneNumber(number='+79266263455', owner=timur_nurmatov)
phone.save()

email = contacts_models.Email(email='tnk@gmail.com', owner=timur_nurmatov)
email.save()

tg_link = contacts_models.TgLink(tg_link='@tnk', owner=timur_nurmatov)
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
    car_mark_model = car_models.CarMark(name=car_mark)
    car_mark_model.save()


car_types = [
    'Грузовик',
    'Легковая',
    'Мотоцикл',
]


for car_type in car_types:
    car_type_model = car_models.CarType(name=car_type)
    car_type_model.save()



# Sample car
car = car_models.Car(
    car_number='a777aa149',
    owner=timur_nurmatov,
    car_type=car_models.CarType.objects.filter(name='Легковая').first(),
    car_mark=car_models.CarMark.objects.all().first()
)


