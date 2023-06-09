from rest_framework import serializers
from .models import Schedules


class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ["id", "loan_id", "function", "execution_date"]
