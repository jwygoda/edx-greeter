import os

from django.conf import settings


def setting(name, default=None):
    try:
        value = getattr(settings, name, os.environ[name])
    except KeyError:
        raise ValueError(f"Set {name} either in settings or environment variables")
    return value
