from .views import ImageViewset
from rest_framework import routers
from django.urls import path, include

app_name = 'api-images'

router = routers.DefaultRouter()
router.register(r'images', ImageViewset)

urlpatterns = [
    path('', include(router.urls))
]
