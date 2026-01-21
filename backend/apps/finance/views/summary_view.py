from django.http import JsonResponse
from django.views import View

class SummaryView(View):
    def get(self, request):
        return JsonResponse({"message": "Summary OK"})
