from django.urls import path
from .views import otavio, kellyson

urlpatterns = [
    path('otavio', otavio, name="otavio"),
    path('kellyson', kellyson, name="kellyson")
]