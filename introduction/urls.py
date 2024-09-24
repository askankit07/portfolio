
from django.urls import path
from introduction import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact_view,name='contact')
]
