from rest_framework import serializers
from django.contrib.auth import get_user_model


class SignupSerializer(serializers.ModelSerializer):
    User = get_user_model()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = self.User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'password']
