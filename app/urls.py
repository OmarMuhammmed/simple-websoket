from django.urls import path
from django.shortcuts import render


def chat_view(request):
    return render(request, 'chat.html')

urlpatterns = [
    path('chat/', chat_view, name='chat'),  
]
