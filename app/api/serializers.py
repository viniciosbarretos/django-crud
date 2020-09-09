from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'title', 'content', 'created_datetime']


    def validate_username(self, value):
        # check if user is trying to change username
        # this is necessary due PUT method, which requires to send all fields to modify object
        if self.instance and value != self.instance.username:
            raise serializers.ValidationError('This field may not be changed.')
        return value