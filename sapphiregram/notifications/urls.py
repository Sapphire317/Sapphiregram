from django.conf.urls import url
from . import views

app_name = 'sapphiregram'

urlpatterns = [
   url(
       regex=r'^$',
       view = views.Notifications.as_view(),
       name='notifications'
   ),
]

