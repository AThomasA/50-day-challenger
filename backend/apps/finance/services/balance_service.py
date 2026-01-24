from apps.finance.services.revenue_service import get_revenue_summary
from apps.finance.services.expense_service import get_expense_summary

def  get_balance(start_date=None, end_date=None):
    revenue_total = get_revenue_summary(start_date, end_date)["total"]
    expense_total = get_expense_summary(start_date, end_date)["total"]
    
    return revenue_total - expense_total