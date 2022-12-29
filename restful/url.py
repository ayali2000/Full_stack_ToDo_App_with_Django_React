from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:pk>', detailAPIview.as_view(), name='detAPIView'),
    path('', PostAPIView.as_view(), name='PostAPIView'),
    # path('GenericAPIView/<int:id>',
    # GenericAPIView.as_view(), name='GenericAPIView'),
]
