from django.urls import include, path
from .views import *

app_name = 'pythonic_chat'
urlpatterns = [
    # path('', chat_index, name='index'),
    path('chat/<str:room_name>', chat, name='chat_room'),
    path('room/', room, name='room'),
]