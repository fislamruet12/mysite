from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Questionserializer
from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuetionView(APIView):
    def get(self,request,format=None):
        data=Question.objects.all()
        serializer=Questionserializer(data,many=True)
        return Response(serializer.data)