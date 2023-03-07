import logging

from rest_framework.generics import CreateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from edx_rest_framework_extensions import permissions
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication

from edx_greeter.models import Greeting
from edx_greeter.rest_api.v1.serializers import GreetingSerializer
from edx_greeter.utils import setting
from edx_rest_api_client.client import OAuthAPIClient

logger = logging.getLogger(__name__)


class GreetingCreateView(CreateAPIView):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
    authentication_classes = (SessionAuthentication, JwtAuthentication)
    permission_classes = (permissions.JWT_RESTRICTED_APPLICATION_OR_USER_ACCESS,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.data.get("text")
        logger.info(f"greeting: {text}")
        if text == "hello":
            client = OAuthAPIClient(
                setting("BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL"),
                setting("BACKEND_SERVICE_EDX_OAUTH2_KEY"),
                setting("BACKEND_SERVICE_EDX_OAUTH2_SECRET"),
            )
            data = client.post(
                setting("GREETING_API_SERVICE_URL"), json={"text": "goodbye"}
            ).json()
            return Response(data)
        else:
            return super().post(request)
