from django.urls import path
from .views import CarListView, CarDetailView

app_name = 'cars'  # Необходимо за именуване на пространството на имена

urlpatterns = [
    path('list/', CarListView.as_view(), name='car_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]
