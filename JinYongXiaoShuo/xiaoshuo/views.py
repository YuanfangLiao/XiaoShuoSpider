from django.shortcuts import render

# Create your views here.
from xiaoshuo.models import XiaoShuo


def index(request):
    articles = XiaoShuo.objects.all()
    titles = []
    for article in articles:
        title = article.title
        if title not in titles:
            titles.append(title)
    return render(request, 'index.html', context={'titles': titles})


def get_caption(request, kw):
    print('获取'+kw)
    captions = XiaoShuo.objects.filter(title=kw).order_by('caption')
    return render(request, 'index.html', context={'captions': captions})

def get_articles(request,title,caption):
    article = XiaoShuo.objects.filter(title=title).filter(caption=caption).first()

    return render(request, 'index.html', context={'article': article})