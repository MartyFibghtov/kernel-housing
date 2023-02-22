from django.urls import include, path
from rest_framework import routers

from housing.views.CarView import car_get_all, car_get_by_id, car_create

from housing.views.EntranceRequestView import entrance_request_get_all, entrance_request_get_by_id, \
    entrance_request_create, entrance_request_delete_by_id

urlpatterns = [
    # path('', index, name='index'),
    # path('', include(router.urls)),
    # path('', include('rest_framework.urls', namespace="rest_framework")),

    # Cars Get Post
    path('cars/get-all/', car_get_all, name='cars/get-all/'),
    path('cars/get-by-id/', car_get_by_id, name='cars/get-by-id/'),
    path('cars/create/', car_create, name='cars/create/'),

    # EntranceRequests Get
    path('entrance-request/get-all/', entrance_request_get_all, name='entrance-request/get-all'),
    path('entrance-request/get-by-id/', entrance_request_get_by_id, name='entrance-request/get-by-id'),
    path('entrance-request/create/', entrance_request_create, name='entrance-request/create'),
    path('entrance-request/delete-by-id/', entrance_request_delete_by_id, name='entrance-request/delete-by-id/'),

]