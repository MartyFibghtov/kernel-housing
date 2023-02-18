from dataclasses import dataclass

from housing.models.address_models import PersonalAccount
from housing.models.car_models import CarMark, CarType, Car
from housing.services.PerosnalAccountService import PersonalAccountService


@dataclass
class CarData:
    car_number: str = None
    id: int = None
    car_type: str = None
    car_mark: str  = None
    owner: str = None


# В дальнейшем выделить отдельные классы для Type и Mark
class CarService:
    # _car: Car

    def __init__(self, car_data: CarData):

        car = Car.objects.filter(car_number=car_data.car_number)


        if car:
            self._car = car[0]
        else:
            self._car = self.create_car(car_data)


    @staticmethod
    def validate_car_data(car_data: CarData):
        CarService.validate_mark(car_data.car_mark)
        CarService.validate_type(car_data.car_type)
        CarService.validate_owner(car_data.owner)


    @staticmethod
    def create_car(car_data: CarData) -> Car:

        car = Car.objects.filter(car_number=car_data.car_number)

        if car:
            raise ValueError("Car already exists")

        CarService.validate_car_data(car_data)
        # If any of parametrs is None - that's either OK or Model will raise exception
        car_mark = CarMark.objects.filter(name__iexact=car_data.car_mark).first()
        car_type = CarType.objects.filter(name__iexact=car_data.car_type).first()
        car_owner = PersonalAccountService.get_by_address(car_data.owner)

        car = Car(
            car_number=car_data.car_number,
            owner=car_owner,
            car_mark=car_mark,
            car_type=car_type
        )

        car.save()

        return car

    @staticmethod
    def validate_number_format(number: str) -> None:
        number_is_correct = True

        if not number_is_correct:
            raise ValueError("Wrong number format!")

    @staticmethod
    def validate_mark(mark: str) -> None:
        if not CarMark.objects.filter(name__iexact=mark).exists():
            raise ValueError("Unknown car mark")

    @staticmethod
    def validate_type(car_type: str) -> None:
        if car_type is None:
            return
        if not CarType.objects.filter(name__iexact=car_type).exists():
            raise ValueError("Unknown car type")

    @staticmethod
    def validate_owner(car_owner):
        if car_owner is None:
            return
        if not PersonalAccountService.validate_address(car_owner):
            raise ValueError("Unknown owner")

    @staticmethod
    def validate_number_exists(car_number):
        if not Car.objects.filter(car_number__iexact=car_number).exists():
            raise ValueError("Unknown car")


