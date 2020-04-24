from rest_framework import serializers
from profiles_api import models


class UserSearializer(serializers.Serializer):
    """ serializer for user class """
    name = serializers.CharField(max_length=10)
    age = serializers.IntegerField(max_value=99, min_value=1)


class UserProfileSerializer(serializers.ModelSerializer):
    """ serializer for profile model"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """ overriden update to save the password using set_password"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            return super().update(instance, validated_data)


class ProfileFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on',)
        extra_kwargs = {
            'user_profile': {
                'read_only': True,
            }
        }
