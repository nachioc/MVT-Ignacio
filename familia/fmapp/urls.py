from django.urls import path
from fmapp.views import lista_familia


urlpatterns = [
    path('' , lista_familia),
]