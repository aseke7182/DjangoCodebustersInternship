from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Company, Review


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    employee_number = serializers.IntegerField(required=True)
    established = serializers.IntegerField(required=True)

    class Meta:
        model = Company
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    ip_address = serializers.IPAddressField(read_only=True)
    submission_date = serializers.DateTimeField(read_only=True)
    company = CompanySerializer()
    reviewer = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
