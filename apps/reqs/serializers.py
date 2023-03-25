from rest_framework import serializers

from apps.reqs.models import RequestModel


class RequestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = (
            'id', 
            'full_name', 
            'email', 
            'phone_number',
            'date_created'
        )
