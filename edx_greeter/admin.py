from django.contrib import admin
from edx_greeter.models import Greeting


class GreetingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Greeting, GreetingAdmin)
