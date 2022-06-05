from django.shortcuts import render
from .models import Detail, Gallery, Certificate, Mission, Vision,Vast_Network,Our_Clients,Board_of_directors,Feathers_to_our_cap
# Create your views here.


def home(request):
	detail = Detail.objects.get()
	ms = Mission.objects.all()
	vs = Vision.objects.all()
	vast = Vast_Network.objects.get()
	cl = Our_Clients.objects.all()
	fs = Feathers_to_our_cap.objects.all()
	context = {
		'detail': detail,
		'ms':ms,
		'vs':vs,
		'vast':vast,
		'cl':cl,
		'fs':fs
	}
	return render(request,'index.html',context)



def gallery(request):
	gallery = Gallery.objects.all()
	context = {
		'gallery': gallery,
	}
	return render(request,'gallery.html',context)



def contact(request):
	ds = Board_of_directors.objects.all()
	context = {
		'ds':ds
	}
	return render(request,'contact.html',context)