from django.contrib.auth.models import User
from rest_framework.viewsets import generics
from drf_spectacular.utils import extend_schema
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.main.serializers import UserRegisterSerializer, UserDeleteFilterSerializer, ChangePasswordSerializer, UpdateUserSerializer
from django.contrib.auth import authenticate


class RegisterView(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id).first()
        return queryset


class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UpdateUserSerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id).first()
        return queryset


class DeleteView(APIView):
    serializer_class = UserDeleteFilterSerializer

    @extend_schema(parameters=[UserDeleteFilterSerializer])
    def delete(self, request):
        filter_serializer = UserDeleteFilterSerializer(data=self.request.GET)
        filter_serializer.is_valid(raise_exception=True)

        username = filter_serializer.validated_data.get('username')
        password = filter_serializer.validated_data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
