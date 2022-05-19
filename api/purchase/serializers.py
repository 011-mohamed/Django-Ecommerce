from .models import Result
from rest_framework import serializers

class ResultSerilazer(serializers.ModelSerializer):
    class Meta:
        model : Result
        fields = ('__all__')