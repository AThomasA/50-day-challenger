from django.urls import path
from .views.expense_view import ExpenseView
from .views.revenue_view import RevenueView
from .views.dashboard_view import DashboardView

urlpatterns = [
    path("expenses/", ExpenseView.as_view(), name="expenses"),
    path("revenues/", RevenueView.as_view(), name="revenues"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
