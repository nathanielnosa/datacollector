from rest_framework import serializers
from django.contrib.auth.models import User
from . models import DataField

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password1','password2','email']
    def verify(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'message':'Password not match'})
    def create(self,validate_data):
        username = validate_data['username']
        password = validate_data['password1']
        email = validate_data['email']
        user = User.objects.create_user(username=username,password=password,email=email)
        return user
