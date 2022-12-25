from django.urls import path
from .views import pIndex

urlpatterns = [
	path('', pIndex)	
]