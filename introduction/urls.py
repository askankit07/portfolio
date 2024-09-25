
from django.urls import path
from introduction import views
urlpatterns = [
    path('',views.home,name='home'),
]
