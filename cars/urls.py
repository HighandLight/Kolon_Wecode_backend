from django.urls import path

from cars.views import CarInformationView

urlpatterns = [
    path('/info', CarInformationView.as_view()),
] 