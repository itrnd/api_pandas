from django.urls import path
from .views import ProfessionalList, ProfessionalDetail


urlpatterns = [
    path('professional', ProfessionalList.as_view()),
    path('professional/<int:pk>', ProfessionalDetail.as_view()),
]
