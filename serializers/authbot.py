from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Code
from django.utils.translation import gettext as _


class LoginSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=100000, max_value=999999)

    def validate_code(self, value):
        code = Code.objects.filter(code=value)
        if not code.exists():
            raise ValidationError(_("Invalid otp code"))
        return code.first()
