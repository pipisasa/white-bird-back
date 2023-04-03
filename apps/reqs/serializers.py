from rest_framework import serializers

from apps.reqs.models import RequestModel


class RequestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = '__all__'
