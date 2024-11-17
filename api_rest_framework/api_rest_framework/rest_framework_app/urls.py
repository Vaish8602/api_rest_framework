from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, UserProjectsViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'user-projects', UserProjectsViewSet, basename='user-projects')

client_router = DefaultRouter()
client_router.register(r'projects', ProjectViewSet, basename='client-projects')

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_pk>/', include(client_router.urls)),
]
