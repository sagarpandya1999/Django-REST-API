from rest_framework import serializers
from status.models import Status

'''
serializers --> can convert data to JSON
serializers --> can also validate data
'''


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'pk',
            'user',
            'content',
            'image'
        ]

    def validate(self , data):
        content = data.get("content",None)
        if content == "":
            content = None
        image = data.get("image",None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required!")
        return data
