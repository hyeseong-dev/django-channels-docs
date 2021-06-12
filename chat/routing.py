# chat/routing.py 는 어디로부터 신호를 받아 오는가?
# 1) urls.py ->
# 2) urls.py -> routing.py -> conusumers.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]