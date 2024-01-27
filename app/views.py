from django.shortcuts import render
from .forms import PostForms
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        items = PostForms(request.POST)
        if items.is_valid():
            title = items.cleaned_data['title']
            text = items.cleaned_data['text']
            status = items.cleaned_data['status']
            if status is "False":
                status = '❌'
            else:
                status = '✅'
            return HttpResponse(f"Title:{title} <br> Text:{text} <br> Status:{status}")

    context = {
            'form':PostForms()
    }
    return render(request, 'home.html', context=context)