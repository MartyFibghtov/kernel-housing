from django.contrib.auth.models import Group

def create_group(group_name):
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print(f"{group_name} group created")
    else:
        print(f"{group_name} group already exist")

create_group('Admin')
create_group('Operator')
create_group('Security')