from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import docs


urlpatterns = [
    path('docs/', include(docs.urlpatterns)),
]
