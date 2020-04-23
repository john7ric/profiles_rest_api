from rest_framework import serializers


class UserSearializer(serializers.Serializer):
    """ serializer for user class """
    name = serializers.CharField(max_length = 10)
    age = serializers.IntegerField(max_value = 99, min_value = 1)