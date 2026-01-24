from django.db.models import Sum, Max, min
from django.db.models.functions import TruncMonth
from apps.finance.models import Revenue

def get_revenue_queryset():
    qs = Revenue.objects.all()
    
    if start_date and end_date:
        qs = qs.filter(received_date__range=(start_date, end_date))
        
    return qs

def get_revenue_summary(start_date=None, end_date=None):
    qs = get_revenue_queryset(start_date, end_date)
    
    return {
       "total": qs.aggregate(total_amount=Sum("amount"))["total_amount"] or 0,
       "max": qs.aggregate(max_amount=Max("amount"))["max_amount"] or 0,
       "min": qs.aggregate(min_amount=min("amount"))["min_amount"] or 0
   }
    
def get_revenue_by_month(start_date=None, end_date=None):
    qs = get_revenue_queryset(start_date, end_date)

    return (
        qs.annotate(month=TruncMonth("received_date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )
    
    