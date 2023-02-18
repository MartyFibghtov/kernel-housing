from housing.models.visitor_models import Human


class HumanService:
    @staticmethod
    def validate_human(name):
        if not Human.objects.filter(number__iexact=name).exists():
            raise ValueError("No such human")