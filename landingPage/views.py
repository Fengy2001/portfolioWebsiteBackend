from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def landingPage(request):
    return render(request, 'landing.html')

@api_view(['GET'])
def get(self, request):
    return Response({"message" : "GET request Processed"})

@api_view(['POST'])
def post(self, request):
    return Response({"message" : "POST request Processed"})