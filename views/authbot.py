from rest_framework.views import APIView
from ..serializers import LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.http.models import User
from core.services import UserService
from core.http.serializers import UserSerializer
from ..management.commands.base import bot
from datetime import datetime


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        ser = LoginSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        code = ser.validated_data.get("code")
        user = code.user
        user, _ = User.objects.get_or_create(
            phone=user.phone,
            defaults={
                "phone": user.phone,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        )
        service = UserService()
        token = service.validate_user(user)
        bot.edit_message_text(
            chat_id=code.user.user_id,
            message_id=code.message_id,
            text="Tasdiqlash ko'di foydalanildi 🫡 ```{}```".format(
                datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            ),
            parse_mode="markdown",
        )
        code.delete()
        return Response(
            {"user": UserSerializer(user).data, "token": token},
            status=status.HTTP_200_OK,
        )
