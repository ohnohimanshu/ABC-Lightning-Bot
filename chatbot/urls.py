# chatbot/urls.py
from django.urls import path
from .views import conversation, chat_interface

urlpatterns = [
    path('converse/', conversation, name='conversation'),
    path('', chat_interface, name='chat_interface'),
]
