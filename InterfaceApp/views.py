from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import PerformanceDB

def index(request):
    context = None
    if request.user.is_authenticated:
        context = {'logineduser' : request.user}
    return render(request, "index.html", context)

def login(request):
    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=useremail, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect("Interface:index")
        else :
            return render(request, 'login.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else :
        return render(request, 'login.html')

def performance(request):

    return render(request, "performance.html")

def signup(request):
    res_data = None
    if request.method == 'POST':
        useremail = request.POST.get('useremail')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        password = request.POST.get('password')
        re_password = request.POST.get('confirm_password')
        res_data = {}
        if User.objects.filter(username=useremail):
            res_data['error'] = '이미 가입된 이메일 주소 입니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username=useremail,
                                            first_name=firstname,
                                            last_name=lastname,
                                            password=password)
            auth.login(request, user)
            return redirect("InterfaceApp:index")
    return render(request, 'signup.html', res_data)


def apitest(request):
    return render(request, 'apitest.html')