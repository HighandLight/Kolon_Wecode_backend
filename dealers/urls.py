from django.urls import path

from dealers.views import SignUpView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
] 