from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):


    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())] )
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'password2',
        )
        read_only_fields = ['id']

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError({
                "detail":"Password Fields didn't match"
            })
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user