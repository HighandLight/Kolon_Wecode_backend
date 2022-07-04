from django.urls import path

from cars.views import CarInformationView, CarMarketPriceView

urlpatterns = [
    path('/info', CarInformationView.as_view()),
    path('/market_price', CarMarketPriceView.as_view()),
] 