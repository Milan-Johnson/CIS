
from django.urls import path
from . import views
# from .filters import StudentFilter

urlpatterns = [
   path('', views.search_details, name = "search")
]
