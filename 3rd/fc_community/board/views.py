from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import BoardForm
from .models import Board
from fcuser.models import Fcuser


# Create your views here.

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        form = BoardForm()
        if form.is_valid():
            user_id = request.session.get['user']
            fcuser = Fcuser.object.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') # 데이터 갖고옴
    page = request.GET.get('p', 1)
    paginator = Paginator(all_boards, 2)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})
