from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':  
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = ProfileForm()
    return render(request, 'index.html',{'form':form})