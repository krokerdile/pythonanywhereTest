from django.shortcuts import render
from datetime import datetime
from .models import Article


def index(request):
    context = {
        'current_date': datetime.now(),
        'title' : 'Home'
    }
    
    return render(request,'index.html',context)


def about(request):
    context = {
        'current_date': datetime.now(),
        'title' : 'About'
    }
    return render(request,'about.html',context)

    
def news(request):
    populate_db()
    articles = get_articles()
    context = {
        'article' : articles,
        'current_date': datetime.now(),
        'title' : 'News'
    }
    return render(request,'news.html',context)

def get_articles():
    result  = Article.objects.all()
    return result

def populate_db():
    if Article.objects.count() == 0:
        Article(title = 'First item', content='This is the first Item in db').save()
        Article(title = 'Second item', content='This is the Second Item in db').save()
        Article(title = 'Third item', content='This is the Third Item in db').save()
        Article(title = 'Fourth item' ,  content= 'This is the Fourth Item in db').save()



