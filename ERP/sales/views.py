from django.shortcuts import render
from django.http import HttpResponse
from sales.models import Customer

# Create your views here.
'''
def cust_fun(request):
	cust_data = Customer.objects.all()
	cust_names = [i.name for i in cust_data]

	return HttpResponse(cust_names)
'''
def cust_fun(request):
	cust_data = Customer.objects.all()
	cust_names = [i.name for i in cust_data]
	return render(request,"cust.html",{"customers":cust_names})