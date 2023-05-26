from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Board

# Create your views here.


def board_list(request):
    boards = Board.objects.all().order_by('-id') # 데이터 갖고옴
    return render(request, 'board_list.html', {'boards': boards})
