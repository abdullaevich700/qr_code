from django.urls import path
from .views import qr_gen_view, dashboard_view

app_name = "qrcode"

urlpatterns = [
    path('', qr_gen_view, name='qr_gen'),
    path('dashboard/', dashboard_view, name='dashboard')
]
