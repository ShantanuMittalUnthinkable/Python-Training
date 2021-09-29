from django.urls import path
from django.urls.conf import include

app_name = "apps"

urlpatterns = [
    path('4/', include('apps.assignment_4.urls', namespace='4')),
    path('5/', include('apps.assignment_5.urls', namespace='5')),
]