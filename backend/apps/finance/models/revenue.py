from django.db import models

class Revenue(models.Model):
    name = models.CharField(max_length=255, verbose_name="Revenue name")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Revenue amount")
    received_date = models.DateField(verbose_name="Date received")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Revenue"
        verbose_name_plural = "Revenues"
        ordering = ['-received_date']
        
    def __str__(self):
        return f"{self.name} - {self.amount}"