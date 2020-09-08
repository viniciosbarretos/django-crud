from django.urls import include, path
from rest_framework import routers
from . import views

# Create DRF Router
router = routers.DefaultRouter()
router.register('', views.PostViewset)

# route to DRF url
urlpatterns = [
    path('', include(router.urls)),
]