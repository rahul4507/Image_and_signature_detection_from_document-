from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  
from .models import ServiceRequest
from .forms import DocumentForm
from Models.process_document import process_document
from Models.image_detection import image_detection
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os



@login_required
def home(request):
    sr = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'home.html', {'service_requests': sr})


@login_required
def service_request_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            scanned_document = request.FILES['document']
    # Save the uploaded file
            direcotry = "inputs"
            file_name = os.path.join(direcotry, scanned_document.name)
            file_name = default_storage.save(file_name, scanned_document)            
            # Get the saved file path
            saved_file_path = default_storage.path(file_name)
            
            # Pass the saved file path to the process_document function
            output_file_path = process_document(saved_file_path) 
            # out_image_path=image_detection(saved_file_path)
            print(output_file_path)
            return render(request, 'home.html', {'sig_detect_path': output_file_path})
    else:
        form = DocumentForm()
    return render(request, 'create.html', {'form': form})