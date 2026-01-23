from django.contrib import admin
from .models import Revenue, Expense

@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "received_date", "create_at",)
    list_filter = ("received_date", "create_at",)
    search_fields = ("name",)
    ordering = ("-received_date",)
    
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "payment_date", "create_at",)
    list_filter = ("payment_date", "create_at",)
    search_fields = ("name",)
    ordering = ("-payment_date",)

