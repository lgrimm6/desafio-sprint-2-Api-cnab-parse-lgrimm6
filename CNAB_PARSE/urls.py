from django.urls import path
from . import views


urlpatterns = [
    path("cnab-auto/", views.CnabAutoView().as_view())
]
