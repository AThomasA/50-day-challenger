from django.http import JsonResponse
from django.views import View

class ExpenseView(View):
    def get(self, request):
        return JsonResponse({"message": "Expenses OK"})
