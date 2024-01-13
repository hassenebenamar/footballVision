# views.py
import os
import pdb
from .footAndBallGit.run_detector import main
from django.shortcuts import render, redirect
from .forms import inputForm, userCreationForm
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required()
def uploadpage(request):
    error_message = None
    if request.method == 'POST':
        form = inputForm(request.POST, request.FILES)
        if form.is_valid():
            # checking if the file is of the correct extension
            uploaded_file = request.FILES['uploaded_File']
            print(uploaded_file.name)
            if uploaded_file.name.endswith(".mp4") or uploaded_file.name.endswith(".avi"):
                instance = form.save()

                # Generate the processed video file
                output_folder = os.path.join(settings.MEDIA_ROOT, 'output')
                os.makedirs(output_folder, exist_ok=True)

                # Use os.path.splitext to get the file name without extension
                file_name, file_extension = os.path.splitext(uploaded_file.name)
                processed_file_name = f"{file_name}-processed.mp4"

                file_path = os.path.join(output_folder, processed_file_name)
                main(uploaded_file, file_path)

                # Send the processed file as a response
                with open(file_path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='video/mp4')  # Adjust content_type
                    response['Content-Disposition'] = f'attachment; filename={processed_file_name}'
                return response
            else:
                error_message = "Wrong file type, only .mp4 or .avi are supported by this application."

        else:
            error_message = "Form is not valid."

    else:
        form = inputForm()

    return render(request, 'upload_page.html', {'form': form, 'error_message': error_message})

@login_required()
def uploadpageML(request):
    error_message = None
    if request.method == 'POST':
        form = inputForm(request.POST, request.FILES)
        if form.is_valid():
            # checking if the file is of the correct extension
            uploaded_file = request.FILES['uploaded_File']
            print(uploaded_file.name)
            if uploaded_file.name.endswith(".csv"):
                instance = form.save()
                return
            else:
                error_message = "Wrong file type, only .csv is supported by this application."

        else:
            error_message = "Form is not valid."

    else:
        form = inputForm()

    return render(request, 'upload_pageML.html', {'form': form, 'error_message': error_message})



def register(request):
    if request.method == 'POST':
        form = userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or do something else after successful registration
            return redirect('success_page')
    else:
        form = userCreationForm()

    return render(request, 'register.html', {'form': form})


def success_page(request):
    return render(request, 'success_page.html')

@login_required()
def dashboard(request):
    if request.method == "POST":
        module_type = request.POST.get('module_type', None)

        if module_type == 'football':
            # Redirect to the 'upload_page' view
            return redirect('upload_page')

        elif module_type == 'machine_learning':
            # Redirect to the 'upload_pageML' view
            return redirect('upload_pageML')

    return render(request, 'dashboard.html')

def loginView(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with the provided email exists
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('dashboard')
        else:
            # Authentication failed, show an error message
            error_message = 'Invalid email or password'
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})

@login_required()
def logoutView(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        logout(request)
        print("nice")
        # Redirect to a login page
        return redirect('login')
    else:
        error_message = None
