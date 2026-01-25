from django.urls import path
from apps.finance.api.views import FinanceDashboardAPIView

urlpatterns = [
    path("dashboard/", FinanceDashboardAPIView.as_view(), name="finance-dashboard-api"),
]
