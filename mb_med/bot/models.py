from django.db import models

class TelegramUsers(models.Model):
    telegram_id = models.CharField(max_length=150, verbose_name='Telegram ID')

    def __str__(self):
        return self.telegram_id


