from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import PerformanceDB, WishlistDB
from django.core.paginator import Paginator
import random

def index(request):
    context = None
    logineduser = False
    if request.user.is_authenticated:
        logineduser = request.user.last_name
    posters = PerformanceDB.objects.values_list('thumbnail', flat=True)
    pick = random.sample(list(posters), 6)
    context = {'logineduser': logineduser,
               'poster1': pick[0],
               'poster2': pick[1],
               'poster3': pick[2],
               'poster4': pick[3],
               'poster5': pick[4],
               'poster6': pick[5],
               }
    return render(request, "index.html", context)

def login(request):
    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=useremail, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect("InterfaceApp:index")
        else :
            return render(request, 'login.html', {'error': '※ 사용자 아이디 또는 패스워드가 틀립니다.'})
    else :
        return render(request, 'login.html')


def performance(request):
    # TODO: 로딩속도 개선 -> 링크 이미지를 파일로 db에 저장??
    # 검색 기능
    if request.GET.get('performance_search'):
        performance_search = request.GET.get('performance_search')     # 검색 결과 받아오기
        performance_lists = PerformanceDB.objects.filter(title__contains=performance_search)  # DB에서 title에 검색 결과가 포함되어 있는 값
    # 지역 선택 기능
    elif request.GET.get('area'):
        area_list = request.GET.getlist('area')
        performance_lists = PerformanceDB.objects.filter(area__in=area_list)  # DB에서 title에 검색 결과가 포함되어 있는 값
        page = request.GET.get('page', 1)  # 페이지
        paginator = Paginator(performance_lists, 10)  # 페이지 당 n개씩 보여주기
        page_obj = paginator.get_page(page)

        # url 중첩 방지를 위한 url path slicing
        current_path = request.get_full_path()
        current_path = current_path[current_path.find('?') + 1:]
        if current_path.find('page') != -1:
            current_path = current_path[:current_path.find('&page')]
        context = {
            'performance_list': page_obj,
            'current_path': current_path,
            'area_list': area_list
        }
        return render(request, "performance.html", context)
        print(area_list)
    # 조회 기능 사용x 시
    else:
        performance_lists = PerformanceDB.objects.all()


    page = request.GET.get('page', 1)  # 페이지
    paginator = Paginator(performance_lists, 10)  # 페이지 당 n개씩 보여주기
    page_obj = paginator.get_page(page)

    # url 중첩 방지를 위한 url path slicing
    current_path = request.get_full_path()
    current_path = current_path[current_path.find('?')+1:]
    if current_path.find('page') != -1:
        current_path = current_path[:current_path.find('&page')]

    context = {
        'performance_list': page_obj,
        'current_path': current_path,
    }
    return render(request, "performance.html", context)

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
            res_data['error'] = '※ 이미 가입된 이메일 주소 입니다.'
        elif password != re_password:
            res_data['error'] = '※ 비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username=useremail,
                                            first_name=firstname,
                                            last_name=lastname,
                                            password=password)
            auth.login(request, user)
            return redirect("InterfaceApp:index")
    return render(request, 'signup.html', res_data)

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("InterfaceApp:index")

def apitest(request):
    return render(request, 'apitest.html')

def wishlist(request):
    #if request.user.is_authenticated:
    #    loggedin_user = request.user.id
    get_list = WishlistDB.objects.all().select_related('performance_seq')
    wish_list = get_list
    print(wish_list)
    context = {
        'wishlist': wish_list,
    }
    return render(request, 'wishlist.html', context)

