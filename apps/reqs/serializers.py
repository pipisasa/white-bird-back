import re

from rest_framework import serializers

from apps.reqs.models import RequestModel


class RequestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = "__all__"

    def validate_phone_number(self, value):

        if value[0] != '+':
            value = '+' + value

        pattern = re.compile(r"^\+(?:[0-9] ?){6,14}[0-9]$")
        if not pattern.match(value):
            raise serializers.ValidationError("Некорректный формат номера телефона")
        return value
