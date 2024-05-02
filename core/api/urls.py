from home.views import index,people
from django.urls import path

urlpatterns = [
   path('index/',index,name = 'index'),
   path('person/',people)
]