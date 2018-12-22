from django.shortcuts import render
from django.contrib import messages
from .paypay_api import paypal


def index(request):
    context = dict()
    if request.method == 'POST':
        kwargs = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'cancel_url': request.POST.get('cancel_url'),
            'return_url': request.POST.get('return_url'),
            'amount': request.POST.get('amount'),
            'frequency': request.POST.get('frequency'),
            'payment_name': request.POST.get('payment_name')
        }
        success, result = paypal.create_billing_plan(**kwargs)
        if success:
            messages.add_message(request, messages.SUCCESS, "Add billing plan success")
        else:
            messages.add_message(request, messages.ERROR, result)

    plans = paypal.get_billing_plans("ACTIVE")
    plans += paypal.get_billing_plans("CREATED")
    context["plans"] = plans
    return render(request, 'index.html', context)
