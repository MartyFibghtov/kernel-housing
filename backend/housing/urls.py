from django.urls import include, path
from rest_framework import routers

from housing.views.address_views import personal_account_get_all, address_get_all, street_get_all
from housing.views.car_views import car_get_all, car_get_by_id, car_create, car_type_get_all, car_mark_get_all

from housing.views.entrance_request_view import entrance_request_get_all, entrance_request_get_by_id, \
    entrance_request_create, entrance_request_delete_by_id

urlpatterns = [
    # Cars Get Post
    path('cars/get-all/', car_get_all, name='cars/get-all/'),
    path('cars/get-by-id/', car_get_by_id, name='cars/get-by-id/'),
    path('cars/create/', car_create, name='cars/create/'),

    # Car marks
    path('cars/types/get-all/', car_type_get_all, name='cars/types/get-all/'),

    # Car types
    path('cars/marks/get-all/', car_mark_get_all, name='cars/marks/get-all/'),


    # EntranceRequests
    path('entrance-request/get-all/', entrance_request_get_all, name='entrance-request/get-all'),
    path('entrance-request/get-by-id/', entrance_request_get_by_id, name='entrance-request/get-by-id'),
    path('entrance-request/create/', entrance_request_create, name='entrance-request/create'),
    path('entrance-request/delete-by-id/', entrance_request_delete_by_id, name='entrance-request/delete-by-id/'),

    # Address
    # Personal account
    path('address/personal-account/get-all/', personal_account_get_all, name='address/personal-account/get-all/'),

    # Streets
    path('address/street/get-all/', street_get_all, name='address/street/get-all/'),

    # Addresses
    path('address/address/get-all/', address_get_all, name='address/address/get-all/'),
]