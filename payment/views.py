from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         client = razorpay.Client(auth=("rzp_test_C3J7evdYwRoSAs", "BcybRfQTm3EoB5fygqz2DihF"))
#         DATA = {
#             "amount": 100,
#             "currency": "INR",
#         }
#         client.order.create(data=DATA)

#     return render(request, 'payment/index.html')

@csrf_exempt
def payment_success(request):
    return render(request, 'payment/payment_success.html')