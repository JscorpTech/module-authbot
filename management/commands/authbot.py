from django.core import management
from .base import bot
from ... import handlers


class Command(management.BaseCommand):

    def handle(self, *args, **options):
        bot.register_message_handler(
            commands=["start"], callback=handlers.start_handler
        )
        bot.register_message_handler(
            content_types=["contact"], callback=handlers.phone_handler
        )
        bot.polling()
        print("Bot Command")
