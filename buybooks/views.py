from django.shortcuts import render

# Create your views here.
def show_test(request):
    context = {}
    return render(request, 'buybooks.html', context)
