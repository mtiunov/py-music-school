from rest_framework import serializers
from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()

    class Meta:
        model = Musician
        fields = "__all__"

    def validate_age(self, value):
        if value < 14:
            raise serializers.ValidationError(
                "We do not accept people who are under 14.")
        return value
