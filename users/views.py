from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request, 'users/index.html')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        try:
            profile = Profile.objects.get_or_create(user = request.user)[0]
        except Exception as e:
            print("Following error occured :", e)
        if request.FILES:
            image = request.FILES["image"]
            profile.image = image
            profile.save()
        if request.POST["first_name"]:
            first_name = request.POST["first_name"]
            user.first_name = first_name
            user.save()
        if request.POST["last_name"]:
            last_name = request.POST["last_name"]
            user.last_name = last_name
            user.save()
        if request.POST["email"]:
            email = request.POST["email"]
            user.email = email
            user.save()
        if request.POST["phonenumber"]:
            phonenumber = request.POST["phonenumber"]
            profile.phonenumber = phonenumber
            profile.save()
        if request.POST["country"]:
            country = request.POST["country"]
            profile.country = country
            profile.save()
        if request.POST["address"]:
            address = request.POST["address"]
            profile.address = address
            profile.save()

        return render(request, 'users/index.html')
        # form = EditProfileForm(request.POST, instance=request.user)
        # profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)  # request.FILES is show the selected image or file

        # if form.is_valid() and profile_form.is_valid():
            # user_form = form.save()
            # custom_form = profile_form.save(False)
            # custom_form.user = user_form
            # custom_form.save()
            # return render(request, 'users/index.html')
        # return render(request, 'users/index.html')
        
    else:
        profile = Profile.objects.get(user = request.user)
        context = {
            "profile":profile
        }
        # form = EditProfileForm(instance=request.user)
        # profile_form = ProfileForm(instance=request.user.profile)
        # args = {}
        # args.update(csrf(request))
        # args['form'] = form
        # args['profile_form'] = profile_form
        return render(request, 'users/edit_profile.html', context)

# @login_required
# def edit_profile_image(request):
#     if request.method == 'POST' and request.FILES['image']:
#         try:
#             profile = Profile.objects.get_or_create(user = request.user)[0]
#         except Exception as e:
#             print("Following error occured :", e)
#         image = request.FILES["image"]
#         profile.image = image
#         profile.save()
#         return render(request, 'users/index.html')
#     return render(request, 'users/index.html')

@login_required
def delete(request):
    User.objects.get(user = request.user).delete()
    return render(request, 'home/login.html')