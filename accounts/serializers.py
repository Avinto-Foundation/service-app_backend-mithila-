from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only =True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','confirm_password','phone_number']
        extra_kwargs = {
            'password' : {'write_only':True},
        }

    def validate_password(self,value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters.")
        return value

    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": ["passwords do not match."]})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            phone_number= validated_data.get('phone_number',''),
        )

        return user 
