from django.urls import path
from .views import otavio

urlpatterns = [
    path('otavio', otavio, name="otavio")
]