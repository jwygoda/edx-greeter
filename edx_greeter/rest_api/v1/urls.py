from django.urls import path

from edx_greeter.rest_api.v1.views import GreetingCreateView

app_name = "v1"

urlpatterns = [path("greeting/", GreetingCreateView.as_view(), name="greeting_create")]
