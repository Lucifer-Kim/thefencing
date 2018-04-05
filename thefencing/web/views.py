from django.shortcuts import render, redirect

from .models import FreePost

import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'index.html')


def fencing(request):
    return fencing_history(request)


def fencing_history(request):
    return render(request, 'fencing_history.html')


def fencing_events(request):
    return render(request, 'fencing_events.html')


def fencing_rules(request):
    return render(request, 'fencing_rules.html')


def fencing_terms(request):
    return render(request, 'fencing_terms.html')


def fencing_club(request):
    return render(request, 'fencing_club.html')


def media_news(request):
    korean_fencing_association = 'http://fencing.sports.or.kr/board/list?code=news'
    r = requests.get(korean_fencing_association, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    news_list = soup.find_all('a', {'class':'pdl10 font-bold'})

    news_dict = {}
    for news in news_list:
        if news.string is not None:
            news_title = news.string.strip()
            news_url = news['data-url']

            news_dict[news_title] = news_url

    return render(request, 'media_news.html', {'news_dict': news_dict})


def fencing_forum(request):

    return redirect(index)


def fencing_photo(request):

    return redirect(index)


def fencing_video(request):

    return redirect(index)


def write_free_board(request):

    return render(request, 'write_free_board.html')


def free_board(request):
    posts = FreePost.objects.all()

    return render(request, 'free_board.html', {'posts': posts})


def write_free_board(request):
    return render(request, 'write_free_board.html')


def qna_board(request):
    return render(request, 'qna.html')


def fleamarket(request):
    return render(request, 'fleamarket.html')


def update(request):
    return render(request, 'update.html')


def contact(request):
    return render(request, 'contact.html')
