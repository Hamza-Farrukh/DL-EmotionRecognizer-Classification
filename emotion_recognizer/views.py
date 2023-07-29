# Built-in
import yaml

# Web
from django.shortcuts import render
from django.http import JsonResponse
from .models import User, File

# Custom
from src.pipeline.predict import Predict


def index(request):
    # if the sent request is POST
    if request.method == 'POST':
        try:
            # Reading the user's info from the configs file
            with open('configs/user_configs.yml', 'r') as configs_file:
                user_configs = yaml.safe_load(configs_file)
                user_configs = user_configs['user_info']
                user_id = user_configs['user_id']
            
            # Deleting the previous image input by the user
            try:
                File.objects.filter(user_id=user_id)[0].delete()
            except:
                pass
            
            # Saving the image's info in the database
            file_upload = request.FILES['imageFile']
            
            file = File()
            file.file_upload = file_upload
            file.user_id = user_id
            file.save()
            
            # Detecting the emotion in the image
            image_path = f"media\{File.objects.filter(user_id=user_id)[0].file_upload}"
            prediction = Predict().predict_with_pretrained(X_input=image_path)
            
            # Sending the response back to the client's side
            return JsonResponse({"success": True, 'message': prediction})
        except Exception as e:
            # Unexpected Error
            return JsonResponse({"success": False, 'message': f'{e}'})
    
    # Rendering the page       
    else:
        return render(request, 'home/index.html')


def login(request):
    # If request is POST
    if request.method == "POST":
        try:
            # Fetching the values from the client's side
            email = request.POST.get("email")
            password = request.POST.get("password")

            # Checking in the database for matching user
            for user in User.objects.all():
                # If all of the credentials match
                if user.email.lower() == email.lower() and user.password == password:
                    # Authentication successful and saving the user's info in a config file 
                    with open('configs/user_configs.yml', 'w') as configs_file:
                        data = {
                            'user_info': {
                                'user_id': user.id,
                                'email': user.email,
                                'name': user.name,
                            }
                        }
                        yaml.dump(data, configs_file)
                    return JsonResponse({"success": True, 'message': 'Login Successful'})
            else:
                # Authentication failed
                return JsonResponse({"success": False, 'message': 'Invalid credentials'})
        except Exception as e:
            # Unexpected Error
            return JsonResponse({"success": False, 'message': f'{e}'})
    # Rendering the page
    else:
        return render(request, 'registration/login.html')


def signup(request):
    # If the request is POST
    if request.method == "POST":
        # Fetching the data from the client's side
        email = request.POST.get("email").lower()
        name = request.POST.get('name')
        password = request.POST.get("password")

        try:
            # Checking the database for the matching user
            for user in User.objects.all():
                if user.email == email:
                    return JsonResponse({"success": False, 'message': 'Email already exists'})
            else:
                # Saving the user in the database
                user = User()
                user.email = email
                user.name = name
                user.password = password
                user.save()
                
                # Sending the response to the client's side
                return JsonResponse({"success": True, 'message': 'Registration Successful'})
        except Exception as e:
            # Unexpected Error
            return JsonResponse({"success": False, 'message': f'{e}'})
    # Rendering the page
    else:
        return render(request, 'registration/signup.html')
