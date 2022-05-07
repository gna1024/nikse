from django.shortcuts import render

# Create your views here.

def aboutus(request):
    if request.user.is_authenticated:
        return render(request, 'aboutus/aboutus.html',{
            "message": 'logout'
        })
    else:
        return render(request, 'aboutus/aboutus.html',{
            "message": 'login'
        })
