from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Expense name")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Expense amount")
    payment_date = models.DateField(verbose_name="Payment date")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
        ordering = ['-payment_date']
        
    def __str__(self):
        return f"{self.name} - {self.amount}"