from django.http import JsonResponse
from django.views import View

class DummyAPIView(View):
    def get(self, request, *args, **kwargs):
        data={
            "id1":"dharmarajjena694@gmail.com","id2":"siliconbaba625@gmail.com"
        }
        return JsonResponse(data)