from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings


app_name = "miPrimerApp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('grupo/cinco/<str:grupo_id>', views.grupoCinco, name="grupoCinco"),
    path('grupo/seis/<str:grupo_id>', views.grupoSeis, name="grupoSeis"),
    path('grupo/siete/<str:grupo_id>', views.grupoSiete, name="grupoSiete")

]

