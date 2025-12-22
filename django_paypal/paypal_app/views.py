from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def checkout(request):
    return render(request, "checkout.html", {
        "paypal_client_id": settings.PAYPAL_CLIENT_ID
    })

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order_id = data.get("id")
        print("Payment successful. Order ID:", order_id)
        return render(request, "payment_success.html")
    else:
        return render(request, "payment_success.html")

def payment_failed(request):
    return render(request, "payment_failed.html")
