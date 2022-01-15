from django.urls import path
from . import views

urlpatterns=[
    path('', views.intro),
    path('stepbystepRecovery', views.stepbystepRecovery),
    path('overseasTripInfo', views.overseasTripInfo),
]