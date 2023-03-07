from django.conf.urls import include
from django.urls import path

app_name = "edx_greeter.rest_api"

urlpatterns = [
    path("v1/", include("edx_greeter.rest_api.v1.urls", namespace="v1")),
]
