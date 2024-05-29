from django.urls import path
from .views import indexfun, regisfun, loginfun, registration, login

urlpatterns = [
    path("", indexfun),
    path("regis_f_o/", regisfun, name="regis_form_open"),
    path("login_f_o/", loginfun, name="login_form_open"),
    path("regis_data_save/", registration, name="regis_data_save"),
    path("login_data_save/", login, name="login_data_save"),
]