from edx_greeter.models import Greeting
from rest_framework import serializers


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = ["text"]
