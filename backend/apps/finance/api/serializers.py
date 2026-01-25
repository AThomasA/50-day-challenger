from rest_framework import serializers


class SummarySerializer(serializers.Serializer):
    total = serializers.DecimalField(max_digits=12, decimal_places=2)
    max = serializers.DecimalField(max_digits=12, decimal_places=2)
    min = serializers.DecimalField(max_digits=12, decimal_places=2)


class MonthlyTotalSerializer(serializers.Serializer):
    month = serializers.DateField()
    total = serializers.DecimalField(max_digits=12, decimal_places=2)


class DashboardSerializer(serializers.Serializer):
    revenue = SummarySerializer()
    expense = SummarySerializer()
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    revenue_by_month = MonthlyTotalSerializer(many=True)
    expense_by_month = MonthlyTotalSerializer(many=True)
