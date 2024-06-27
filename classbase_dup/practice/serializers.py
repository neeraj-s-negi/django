from rest_framework import serializers
from .models import Student, CustomUser

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','section','state','phone_no']



# class CustomStudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
        # fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')


# class CustomBaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomBaseUser