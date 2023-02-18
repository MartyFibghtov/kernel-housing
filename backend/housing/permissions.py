from rest_framework import permissions


class SecurityPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        security_group_name = 'Security'

        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name=security_group_name).exists():
            return True

        return False

class OperatorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        operator_group_name = 'Operator'

        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name=operator_group_name).exists():
            return True

        return False