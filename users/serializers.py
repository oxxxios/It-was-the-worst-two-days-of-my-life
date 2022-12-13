from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "phone first_name last_name password".split()

    def create(self, validated_data):
        user = User.objects.create_user(
            phone=validated_data["phone"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    phone = PhoneNumberField()
    password = serializers.CharField()
