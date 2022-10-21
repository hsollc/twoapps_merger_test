from collections import OrderedDict

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import PerformanceDB, WishlistDB
from django.core.paginator import Paginator
import random
<<<<<<< HEAD
import math
=======
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
>>>>>>> f86b8ef0274a4e90b21d30cc9453986b3d003c81

def index(request):
    context = None
    logineduser = False
    if request.user.is_authenticated:
        logineduser = request.user.first_name + request.user.last_name
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
        return render(request, 'login.html',)


def performance(request):
    # TODO: 로딩속도 개선 -> 링크 이미지를 파일로 db에 저장??
    # 검색 기능
    if request.GET.get('performance_search'):
        performance_search = request.GET.get('performance_search')     # 검색 결과 받아오기
        performance_lists = PerformanceDB.objects.filter(title__contains=performance_search)  # DB에서 title에 검색 결과가 포함되어 있는 값
    # 기간 선택 기능
    elif request.GET.get('date'):
        date_search = request.GET.get('date')     # 검색 결과 받아오기
        performance_lists = PerformanceDB.objects.filter(startDate__lte=date_search, endDate__gte=date_search)  # DB에서 title에 검색 결과가 포함되어 있는 값
        print(request.GET.get('date'))
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
    # 분류 선택 기능
    elif request.GET.get('classification'):
        classification_list = request.GET.getlist('classification')
        performance_lists = PerformanceDB.objects.filter(realmName__in=classification_list)  # DB에서 title에 검색 결과가 포함되어 있는 값
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
            'classification_list': classification_list
        }
        return render(request, "performance.html", context)
    # 정렬 선택 기능
    elif request.GET.get('orderby'):
        orderby_list = request.GET.getlist('orderby')
        if orderby_list[0] == '거리':
            current_latitude = float(request.GET.get('latitude'))
            current_longitude = float(request.GET.get('longitude'))
            distanceDict = OrderedDict()
            for i in range(len(PerformanceDB.objects.all())):
                distanceDict[PerformanceDB.objects.all().values()[i]['seq']] = math.sqrt((current_latitude-PerformanceDB.objects.all().values()[i]['gpsY'])**2 + (current_longitude-PerformanceDB.objects.all().values()[i]['gpsX'])**2)
            distanceDict = dict(sorted(distanceDict.items(), key=lambda x: x[1]))
            orderby_distance_list = list(distanceDict)
            orderby_lists = PerformanceDB.objects.filter(seq=orderby_distance_list[0])
            print(orderby_lists)
            for i in range(1, len(PerformanceDB.objects.all())):
                orderby_lists = orderby_lists|PerformanceDB.objects.filter(seq=orderby_distance_list[i])
        elif orderby_list[0] == '제목':
            orderby_lists = PerformanceDB.objects.all().order_by('title')
        elif orderby_list[0] == '시작일':
            orderby_lists = PerformanceDB.objects.all().order_by('startDate')
        elif orderby_list[0] == '마감일':
            orderby_lists = PerformanceDB.objects.all().order_by('endDate')
        page = request.GET.get('page', 1)  # 페이지
        paginator = Paginator(orderby_lists, 10)  # 페이지 당 n개씩 보여주기
        page_obj = paginator.get_page(page)

        # url 중첩 방지를 위한 url path slicing
        current_path = request.get_full_path()
        current_path = current_path[current_path.find('?') + 1:]
        if current_path.find('page') != -1:
            current_path = current_path[:current_path.find('&page')]
        context = {
            'performance_list': page_obj,
            'current_path': current_path,
            'orderby_list': orderby_list
        }
        return render(request, "performance.html", context)
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
    context = None
    user_id = request.user.id
    wish_list = []
    get_list = WishlistDB.objects.filter(user_id=user_id)
    #pk = get_list.values('id')
    for i in range(len(get_list)):
        wish_list.append(get_list[i].performance_seq)

    context = {
        'wishlist': wish_list,
        #'pk': pk,
    }
    return render(request, 'wishlist.html', context)

@csrf_exempt
def add_wishlist(request):
    data = json.loads(request.body)
    wish_item = data['performance_seq']
    user_id = request.user.id

    get_list = WishlistDB.objects.filter(user_id=user_id)
    print(get_list.values_list('performance_seq', flat=True))
    if wish_item not in get_list.values_list('performance_seq', flat=True):
        row = WishlistDB(user_id=User.objects.get(pk=user_id), performance_seq=PerformanceDB.objects.get(pk=wish_item))
        row.save()
    #else:
        #row = WishlistDB.objects.get(performance_seq=wish_item)
        #row.delete()
    return render(request, 'performance.html')

@csrf_exempt
def del_wishlist(request):
    data = json.loads(request.body)
    wish_item = data['performance_seq']
    user_id = request.user.id

    row = WishlistDB.objects.get(user_id=user_id, performance_seq=wish_item)
    row.delete()

    return render(request, 'wishlist.html')

def mypage(request):
    return render(request, 'mypage.html')

def profile(request):
    return render(request, 'profile.html')
