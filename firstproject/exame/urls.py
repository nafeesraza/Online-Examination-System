from django.urls import path
from . import views
urlpatterns=[
    path('test-paper/',views.testpaper),
    path('test-result/',views.testresult),
]
