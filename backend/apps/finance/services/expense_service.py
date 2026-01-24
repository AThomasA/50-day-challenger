from django.db.models import Sum, Max, Min
from django.db.models.functions import TruncMonth
from apps.finance.models import Expense


def get_expense_queryset(start_date=None, end_date=None):
    qs = Expense.objects.all()

    if start_date and end_date:
        qs = qs.filter(payment_date__range=(start_date, end_date))

    return qs


def get_expense_summary(start_date=None, end_date=None):
    qs = get_expense_queryset(start_date, end_date)

    return {
        "total": qs.aggregate(total=Sum("amount"))["total"] or 0,
        "max": qs.aggregate(max=Max("amount"))["max"] or 0,
        "min": qs.aggregate(min=Min("amount"))["min"] or 0,
    }


def get_expense_by_month(start_date=None, end_date=None):
    qs = get_expense_queryset(start_date, end_date)

    return (
        qs.annotate(month=TruncMonth("payment_date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )
