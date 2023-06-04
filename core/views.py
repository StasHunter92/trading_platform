from django.contrib.auth import authenticate, login, logout
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import User
from core.serializers import UserSignupSerializer, UserLoginSerializer, UserRetrieveUpdateSerializer


# ----------------------------------------------------------------------------------------------------------------------
# User views
@extend_schema(summary='Регистрация пользователя', tags=['Пользователи'])
class UserSignupView(CreateAPIView):
    """Create a new user"""

    queryset = User.objects.all()
    serializer_class = UserSignupSerializer


# -----------------------------------------------------------------------------
@extend_schema(summary='Авторизация пользователя', tags=['Пользователи'])
class UserLoginView(CreateAPIView):
    """Login user"""

    serializer_class = UserLoginSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Method to check input user data and login user
        Returns:
            Success response or Failure response with error
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username: str = serializer.validated_data['username']
        password: str = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)

        raise AuthenticationFailed('Wrong username or password')


# -----------------------------------------------------------------------------
@extend_schema(tags=['Пользователи'])
class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """View for retrieving user information, updating or logout user"""

    serializer_class = UserRetrieveUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> any:
        return self.request.user

    @extend_schema(summary='Профиль пользователя')
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

    @extend_schema(summary='Обновление пользователя')
    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(summary='Логаут пользователя')
    def delete(self, request: Request, *args, **kwargs) -> Response:
        """
        Logout user from application
        Returns:
            204 No content response
        """

        logout(request)

        return Response(status=status.HTTP_204_NO_CONTENT)
