from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error':'Age cannot be less than 18'})
        
        special_characters='-\'"!@#$%^&*()_+=<>?/\\,.;:{}\[\]]+$'
        if any (c in  special_characters for c in data['name']):
            raise serializers.ValidationError("Name contains special characters")
        
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
