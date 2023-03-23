from django.core.management.base import BaseCommand

from ...loader import my_bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        from ... import handlers
        print('Bot ishga tushdi...')
        my_bot.infinity_polling()


