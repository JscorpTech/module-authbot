from core.http.models import AbstractBaseModel
from django.db import models
from random import randint
from tenacity import retry, stop_after_attempt


class BotUser(AbstractBaseModel):
    user_id = models.BigIntegerField()
    first_name = models.CharField(max_length=1000, null=True, blank=True)
    last_name = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.phone


class CodeManager(models.Manager):

    @retry(stop=stop_after_attempt(10))
    def get_or_create_code(self, user_id):
        return self.get_or_create(
            user_id=user_id, defaults={"code": randint(100000, 999999)}
        )[0]


class Code(AbstractBaseModel):
    code = models.BigIntegerField(unique=True)
    message_id = models.BigIntegerField(null=True, blank=True)
    user = models.OneToOneField(BotUser, on_delete=models.CASCADE)

    objects = CodeManager()

    def __str__(self) -> str:
        return str(self.code)
