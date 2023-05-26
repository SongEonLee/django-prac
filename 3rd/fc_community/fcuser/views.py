from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm
from .models import Fcuser


# Create your views here.

def home(request):
    user_id = request.session.get('user')
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('Home')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form}) # 템플릿에 폼 전달

    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
    #
    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야함'
    #     else:
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password, fcuser.password):
    #             # 세션
    #             request.session['user'] = fcuser.id
    #             # 리다이렉트
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호 틀림'
    #
    #     return render(request, 'login.html', res_data)

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html') # template폴더 안에서 파일을 찾음
    elif request.method == 'POST':
        username = request.POST.get('username', None) # get함수로 키의 기본값 none지정
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        email = request.POST.get('useremail', None)

        res_data = {}
        if not (username and email and password and re_password):
            res_data['error'] = '모든 값을 입력해야함'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username = username,
                password = make_password(password),
                useremail = email
            )
            fcuser.save()

        return render(request, 'register.html', res_data)