from dataclasses import dataclass

from housing.models.address_models import PersonalAccount
from housing.models.car_models import CarMark, CarType, Car
from housing.models.entrance_request_models import EntranceRequest
from housing.services.CarService import CarData, CarService
from housing.services.PerosnalAccountService import PersonalAccountService

@dataclass
class EntranceRequestData:
    request_account: str
    car: CarData
    is_car: bool
    is_paid: bool
    # Not required fields
    note: str = None
    date_created: str = None

class EntranceRequestService:
    #TODO For cars and humans

    # _entrance_request = EntranceRequest
    def __init__(self, entrance_request_data: EntranceRequestData):
        self._entrance_request = self.create_entrance_request(entrance_request_data)

    @staticmethod
    def validate_entrance_request_data(entrance_request_data: EntranceRequestData):
        PersonalAccountService.validate_address(entrance_request_data.request_account)
        if not Car.objects.filter(pk=entrance_request_data.car.id).exists():
            raise ValueError("Unknown car id")

    @staticmethod
    def create_entrance_request(entrance_request_data: EntranceRequestData):
        erd = entrance_request_data
        EntranceRequestService.validate_entrance_request_data(erd)

        request_account = PersonalAccountService.get_by_address(erd.request_account)
        car = Car.objects.get(pk=erd.car.id)

        entrance_request = EntranceRequest(
            request_account=request_account,
            is_car=erd.is_car,
            car=car,
            is_paid=erd.is_paid,
            note=erd.note
        )

        entrance_request.save()

        return entrance_request