from celery import shared_task
from ..models import Code
from datetime import timedelta, datetime
from ..management.commands.base import bot


@shared_task
def clear_old_codes():
    codes = Code.objects.filter(
        created_at__lte=datetime.now() - timedelta(minutes=10)
    )
    if codes.exists():
        for code in codes:
            bot.edit_message_text(
                chat_id=code.user.user_id,
                message_id=code.message_id,
                text="Tasdiqlash ko'dining muddati tugadi 🙁",
            )
            return code.delete()
