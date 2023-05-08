from rest_framework import serializers
from .models import Professional


class ProfessionalSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(input_formats=["%d/%m/%Y"], format="%d/%m/%Y")

    class Meta:
        model = Professional
        fields = '__all__'


