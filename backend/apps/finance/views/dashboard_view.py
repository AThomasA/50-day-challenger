from django.shortcuts import render
from apps.finance.services.revenue_service import get_revenue_summary, get_revenue_by_month
from apps.finance.services.expense_service import get_expense_summary, get_expense_by_month
from apps.finance.services.balance_service import get_balance

def finance_dashboard(request):
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    
    revenue = get_revenue_summary(start_date, end_date)
    expense = get_expense_summary(start_date, end_date)
    
    context = {
        "revenue": revenue,
        "expense": expense,
        "balance": get_balance(start_date, end_date),
        "revenue_by_month": get_revenue_by_month(start_date, end_date),
        "expense_by_month": get_expense_by_month(start_date, end_date),
        "start_date": start_date,
        "end_date": end_date,
    }
    
    return render(
        request,
        "finance/dashboard.html",
        context
    )