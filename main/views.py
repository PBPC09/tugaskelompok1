from django.shortcuts import render

# Create your views here.
def show_landing_page(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }
    return render(request, "landingpage.html", context)