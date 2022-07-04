from django.urls import path, include

urlpatterns = [
    path('dealers', include('dealers.urls')),
    path('cars', include('cars.urls')),
]