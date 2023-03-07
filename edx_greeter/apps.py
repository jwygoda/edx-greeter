from django.apps import AppConfig


class EdxGreeterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "edx_greeter"
    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "edx-greeter",
                "regex": "^api/edx_greeter/",
                "relative_path": "rest_api.urls",
            }
        },
    }


class EdxGreeterCMSConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "edx_greeter"
    plugin_app = {
        "url_config": {
            "cms.djangoapp": {
                "namespace": "edx-greeter",
                "regex": "^api/edx_greeter/",
                "relative_path": "rest_api.urls",
            }
        },
    }
