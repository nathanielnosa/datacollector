from rest_framework import serializers
from django.contrib.auth.models import User
from . models import DataField

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password1','password2','email','first_name','last_name']
    def validate(self, data):
        if not data['first_name']:
            raise serializers.ValidationError({'message':'This field is required'})
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'message':'Password not match'})
        return data
    def create(self,validate_data):
        username = validate_data['username']
        password = validate_data['password1']
        email = validate_data['email']
        first_name = validate_data['first_name']
        last_name = validate_data['last_name']
        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        return user

class DataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataField
        fields = '__all__'
        read_only_fields = ['user','status','created_at']
    def validate(self,value):
        if not value['location']:
            raise serializers.ValidationError({"message":"This field is required."})
        if not value['amount_paid'] or value['amount_paid'] <= 0:
            raise serializers.ValidationError({"message":"Amount paid must be greater than zero."})
        if not value['volume_dispensed'] or value['volume_dispensed'] <= 0:
            raise serializers.ValidationError({"message":"Volume dispensed must be between 1 and 1000."})
        return value