from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('track_request', request_id=new_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/submit_request.html', {'form': form})
def track_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id, user=request.user)
    return render(request, 'customer/track_request.html', {'service_request': service_request})
