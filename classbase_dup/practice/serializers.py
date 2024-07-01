from rest_framework import serializers
from .models import Student, CustomUser
from django.core.validators import validate_email
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from practice.models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model, authenticate, password_validation
from django.core import exceptions

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','section','state','phone_no']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token
    

# Overriding a default User Create Serializer
class RegisterSerializer(serializers.ModelSerializer):
    '''Serializer for creating a new user'''
    password = serializers.CharField(
        write_only=True, min_length=8, required=True)
    password2 = serializers.CharField(
        write_only=True, min_length=8, required=True)

    def validate(self, attrs):
        try:
            if CustomUser.objects.filter(email=attrs['email']).exists():
                raise serializers.ValidationError('This Email is Already Used')

            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError('This Password Not Match')

            else:
                password_validation.validate_password(attrs['password'])
                validate_email(attrs['email'])

        except exceptions.ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return attrs


    def create(self, validated_data):
        validated_data.pop('password2', None)
        return CustomUser.objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'email', 'first_name', 'last_name', 'password', 'password2','is_staff',
        ]

        read_only_fields = ['id',]
        extra_kwargs = {

            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
        }



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User is deactivated.')
            else:
                raise serializers.ValidationError('Invalid credentials.')
        else:
            raise serializers.ValidationError('Must provide both email and password.')

        return data



# class CustomStudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
        # fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

