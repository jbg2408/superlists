from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    # when we call the views.py, we render the home.html page
    # we pass to it a variable 'new_item_text" which is set to
    # the value in item_text (from the form) or and empty string
    # The value is set when return (ENTER) is hit
    return render(request, 'home.html', {
        'new_item_text' : request.POST.get('item_text', ''),
    })
