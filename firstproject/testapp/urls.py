from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.greeting),
    path('about/',views.about),
    path('contactus/',views.contactus),
]
