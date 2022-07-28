from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
#from clients.views import ClientViewSet
#from events.views import EventViewSet
#from contracts.views import ContractViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

"""
router = SimpleRouter()

router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'contracts', ContractViewSet, basename="contracts")
router.register(r'events', EventViewSet, basename='events')"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    #path(r'', include(router.urls)),
]
