from unittest import TestResult
from django.urls import path
from .views import *
urlpatterns=[
    path('new-question/',newQuestion),
    path('save-question/',saveQuestion),
    path('view-questions/',viewQuestions),
    path('edit-question/',editQuestion),
    path('save-edit-question/',saveEditQuestion),
    path('delete-question/',deleteQuestion),
    path('signup/',signup),
    path('save-user/',saveUser),
    path('login-validation/',loginValidation),
    path('login/',login),
    path('logout/',logout),
    path('home/',home),
    path('start-test/',startTest),
    path('test-result/',testResult),
]
