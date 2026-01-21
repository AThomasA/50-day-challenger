from django.urls import path
from .views.expense_view import ExpenseView
from .views.revenue_view import RevenueView
from .views.summary_view import SummaryView

urlpatterns = [
    path("expenses/", ExpenseView.as_view(), name="expenses"),
    path("revenues/", RevenueView.as_view(), name="revenues"),
    path("summary/", SummaryView.as_view(), name="summary"),
]
