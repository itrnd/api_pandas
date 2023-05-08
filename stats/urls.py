from django.urls import path
from .views import AgeStats, SalaryStats


urlpatterns = [
    path('age', AgeStats.as_view()),
    path('salary', SalaryStats.as_view()),
]
