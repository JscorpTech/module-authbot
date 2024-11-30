from ..models import BotUser
from ..management.commands.base import bot
from ....http.models import SmsConfirm


class BotService:

    def __init__(self) -> None: ...

    def send_sms(self, phone_number, message):
        user = BotUser.objects.filter(phone=phone_number)
        print(user)
        if not user.exists():
            SmsConfirm.objects.filter(phone=phone_number).delete()
            return
        user = user.first()
        bot.send_message(user.user_id, message)
