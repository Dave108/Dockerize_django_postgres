from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Details

# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('text')
        print(name)
        if name:
            detail_obj = Details.objects.create(name=name)
        else:
            return HttpResponseRedirect(reverse('home_page'))
        all_details = Details.objects.all()
        context = {
            "name":detail_obj.name,
            "created_at":detail_obj.created_at,
            "all_details":all_details,
        }
    return render(request, 'homepage.html', context)