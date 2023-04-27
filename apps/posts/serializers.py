from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    img = serializers.ReadOnlyField(source='img.url')

    class Meta:
        model = Post
        fields = '__all__'
