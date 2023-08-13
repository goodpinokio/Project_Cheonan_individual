from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

# Create your views here.
def about_me(request):
    if request.user.is_authenticated:
        user_posts = Post.objects.filter(author=request.user).order_by('-pk')
    else:
        user_posts = []  # 빈 리스트 할당
    
    paginator = Paginator(user_posts, 3)  # 페이지당 3개의 글을 보여줌
    page_number = request.GET.get('page')  # 현재 페이지 번호 가져오기
    page_obj = paginator.get_page(page_number)  # 현재 페이지 객체 가져오기
    
    recent_posts = Post.objects.order_by('-pk')[:3]  # 최신 글 3개 가져오기
    
    return render(
        request,
        'single_pages/about_me.html',
        {
            'recent_posts': recent_posts,
            'page_obj': page_obj,  # 페이지네이션을 위한 page_obj 변수 추가
        }
    )