from rest_framework.authentication import get_authorization_header, BaseAuthentication
import jwt
from django.conf import settings
from rest_framework import exceptions
from authentication.models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode("utf-8").split(" ")
        if not auth_data or auth_data[0].lower() != "bearer":
            raise exceptions.AuthenticationFailed("Token not valid")
        try:
            token = auth_data[1]
        except IndexError:
            raise exceptions.AuthenticationFailed("Token not valid")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            username = payload["username"]
            user = User.objects.get(username=username)
        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed("No such user")
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Token Expired")
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed("Token not valid")
        return (user, token)
