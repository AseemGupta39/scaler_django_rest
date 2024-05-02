from rest_framework import serializers
from home.models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = '__all__'
        # exclude = ['name']
        fields = ['name','age']
    