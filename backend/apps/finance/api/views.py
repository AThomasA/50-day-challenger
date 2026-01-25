from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.finance.services.revenue_service import (
    get_revenue_summary,
    get_revenue_by_month
)
from apps.finance.services.expense_service import (
    get_expense_summary,
    get_expense_by_month
)
from apps.finance.services.balance_service import get_balance

from apps.finance.api.serializers import DashboardSerializer


class FinanceDashboardAPIView(APIView):
    """
    Finance Dashboard API
    """

    def get(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        data = {
            "revenue": get_revenue_summary(start_date, end_date),
            "expense": get_expense_summary(start_date, end_date),
            "balance": get_balance(start_date, end_date),
            "revenue_by_month": get_revenue_by_month(start_date, end_date),
            "expense_by_month": get_expense_by_month(start_date, end_date),
        }

        serializer = DashboardSerializer(data)

        return Response(serializer.data, status=status.HTTP_200_OK)
