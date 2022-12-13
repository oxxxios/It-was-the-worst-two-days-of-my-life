from users.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import APIView
from users.serializers import LoginSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken



class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(**serializer.data)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)

            return Response(data={
                "status": status.HTTP_200_OK,
                "user": user.first_name,
                "refresh": str(refresh),
                "access": str(access)
                })
