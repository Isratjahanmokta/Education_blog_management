from rest_framework import serializers
from Auth.models import CustomUser
from django.contrib.auth import get_user_model


class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
                'first_name',
                'last_name',
                'username',
                'password',
                'email',
                'is_student',]
                
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(password)
        user.save()
        return user

