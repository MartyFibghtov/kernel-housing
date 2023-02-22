# from dataclasses import dataclass
#
# from housing.models.AddressModels import PersonalAccount
# from housing.models.CarModels import Car
# from housing.models.EntranceRequestModels import EntranceRequest
# from housing.models.VisitorModels import Human
#
# from housing.services.CarService import CarService
# from housing.services.HumanService import HumanService
#
#
#
# @dataclass
# class EntranceRequestData:
#     request_account: str
#
#     car_number: str | None
#     human_name: str | None
#
#     is_car: bool
#     is_paid: bool | None
#     note: str | None
#
#
# class EntranceRequestService:
#     def __init__(self, gate_request_data: EntranceRequestData):
#         self._validate(gate_request_data)
#         self._request = self.create_entrance_request(gate_request_data)
#
#     def create_entrance_request(self, gate_request_data: EntranceRequestData) -> EntranceRequest:
#         request_account = PersonalAccount.objects.filter(
#             address__name__iexact=gate_request_data.request_account).first()
#
#         car = None
#         human = None
#         if gate_request_data.is_car:
#             car = Car.objects.filter(number__iexact=gate_request_data.car_number).first()
#         else:
#             human = Human.objects.filter(number__iexact=gate_request_data.human_name).first()
#
#         is_paid = False
#         if gate_request_data.is_paid:
#             is_paid = True
#
#         request = EntranceRequest(
#             request_account=request_account,
#
#             car=car,
#             human=human,
#             is_car=gate_request_data.is_car,
#             is_paid=is_paid,
#             note=EntranceRequest.note
#         )
#         request.save()
#
#         return request
#
#
#     def _validate(self, gate_request_data: EntranceRequestData) -> None:
#         PersonalAccount.validate_personal_account(gate_request_data.request_account)
#         # TODO Forbidden access
#
#         if gate_request_data.is_car:
#             CarService.validate_number_exists(gate_request_data.car_number)
#         else:
#             HumanService.validate_human(gate_request_data.human_name)
