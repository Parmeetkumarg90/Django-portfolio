from django.http import HttpResponse
from django.shortcuts import render
from skill.models import newskill
from contactform.models import contact_data

def home(request):
    skill_obj = newskill.objects.all()
    print(request.POST)  # This will show you the keys in the POST data
    try:
        obj = contact_data(
            user_name=request.POST['name'],
            user_phone=request.POST['mobile'],
            user_email=request.POST['email'],
            user_message=request.POST['message']
        )
        obj.save()
    except KeyError as e:
        print(f"KeyError: {e}")
    if (skill_obj.exists()):
        return render(request, 'index.html',{'skill_obj':skill_obj})
    else:
        return render(request,'index.html')