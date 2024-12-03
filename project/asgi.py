import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from app.routing import websocket_urlpatterns # the same job file urls.py 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# project can see HTTP requests and websockets requests 
application = ProtocolTypeRouter({
    # catch HTTP requests
    "http": get_asgi_application(), 
    # catch websockets requests 
    "websocket": AuthMiddlewareStack( # middleware to check authentaction system 
        URLRouter(
            websocket_urlpatterns # path websocket
        )
    ),
})
