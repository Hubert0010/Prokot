from django.urls import path
from .views import sign_up, sign_in, dashboard, logout

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('logout/', logout, name='log_out'),
]
