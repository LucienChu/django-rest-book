from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
app_name = "drink"

urlpatterns = [
    path('', views.drink_list),
    path('<int:id>/', views.drink_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)