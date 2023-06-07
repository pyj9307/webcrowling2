from django.shortcuts import render
from django.views.generic.list import ListView
from bookmark.models import Bookmark
from django.views.generic.detail import DetailView
from django.template.context_processors import request

# Create your views here.
def home(request):
    # select * from  bookmark_bookmark order by title
    urlList=Bookmark.objects.all().order_by("title") # -title 내림차순 정렬
    # select count(*) from bookmark_bookmark
    urlCount=Bookmark.objects.all().count()
    
    return render(request, 'bookmark/list.html',{'urlList':urlList,'urlCount':urlCount})

def detail(request):
    addr=request.GET['url']
    # select * from bookmark_bookmark where url=addr
    dto=Bookmark.objects.get(url=addr)
    
    return render(request, 'bookmark/detail.html',{'dto':dto})

# class BookmarkLV(ListView):
#     model=Bookmark
#     # bookmark_list.html 에 알아서 object_list 반환
#
# class BookmarkDV(DetailView):
#     model=Bookmark