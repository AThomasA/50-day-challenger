from django.http import JsonResponse
from django.views import View

class RevenueView(View):
    def get(self, request):
        return JsonResponse({"message": "Revenues OK"})