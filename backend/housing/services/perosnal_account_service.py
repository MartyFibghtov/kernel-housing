from housing.models.address_models import PersonalAccount, Address, Street
import re

class StreetService:
    @staticmethod
    def verify_short_street_name(short_street_name: str, is_short_name=True):
        if not is_short_name:
            raise NotImplementedError()

        if not Street.objects.filter(short_street_name=short_street_name).exists():
            raise ValueError("No such short name")

    @staticmethod
    def get_street_by_name(name, is_short_name=True):
        if not is_short_name:
            raise NotImplementedError()

        if is_short_name:
            return Street.objects.filter(short_name=name).first()

class AddressService:

    @staticmethod
    def read_from_str(address_name: str) -> Address:
        value_error = ValueError(f"Wrong address name format {address_name}")

        address_name_regex = r"([А-Яа-я]+)\s(\d+)/(\d+)"
        re_match = re.match(address_name_regex, address_name)

        if not re_match:
            raise value_error

        # try:
        street_short = re_match.group(1)
        street = StreetService.get_street_by_name(street_short, is_short_name=True)
        house_number = int(re_match.group(2))
        flat_number = int(re_match.group(3))

        return Address(
            street=street,
            house_number=house_number,
            flat_number=flat_number
        )

        # except ValueError:
        #     raise ValueError("Wrong address")

    @staticmethod
    def validate_address(address_name: str):
        address = AddressService.read_from_str(address_name)
        if not Address.objects.filter(
                street=address.street,
                house_number=address.house_number,
                flat_number=address.flat_number
        ).exists():
            raise ValueError("Wrong address")
        return True

    @staticmethod
    def get_address(address_name: str) -> Address:
        address = AddressService.read_from_str(address_name)
        address = Address.objects.filter(
                street=address.street,
                house_number=address.house_number,
                flat_number=address.flat_number
        ).first()
        return address

class PersonalAccountService:
    # _personal_account:
    @staticmethod
    def validate_address(address) -> bool:
        return AddressService.validate_address(address)

    @staticmethod
    def get_by_address(address_name):
        address: Address = AddressService.get_address(address_name)
        return PersonalAccount.objects.filter(address=address).first()



