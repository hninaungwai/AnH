from django.shortcuts import render
from .models import Pharmacy
# Create your views here.
def home(request):
	myshop = Pharmacy.objects.all()
	context = {
		'myshop' :myshop
	}
	return render(request, 'shop/index.html', context)

def contact(request):
	return render(request, 'shop/contact.html')