from ..models import Code, BotUser
from django.contrib import admin
from unfold.admin import ModelAdmin


admin.site.register(Code, ModelAdmin)
admin.site.register(BotUser, ModelAdmin)
