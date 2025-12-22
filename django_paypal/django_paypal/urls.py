from django.contrib import admin
from django.urls import path
from paypal_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("checkout/", views.checkout, name="checkout"),
    path("success/", views.payment_success, name="payment_success"),
    path("failed/", views.payment_failed, name="payment_failed"),
]
