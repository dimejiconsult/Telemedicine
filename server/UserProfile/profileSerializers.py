from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Profile, DoctorProfile


#<---- Profile Serializer ------->#
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'email', 'first_name', 'last_name']

#<---- Doctor Serializers------>
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'


#<---- Resgister New User ------->
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Profile
        fields = ["first_name","last_name","email", "password"]
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = Profile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    

#<---- Login New User ------->
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials: Username or Password")