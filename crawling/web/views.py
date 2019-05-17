from django.shortcuts import render
from web.forms import SearchForm
from django.views.generic.edit import FormView
import requests
from bs4 import BeautifulSoup

# Create your views here.
class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'search.html'
    
    def form_valid(self, form): # post method로 값이 전달 됬을 경우
        URL = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
        word = self.request.POST['word'] # 검색어
        fullURL = URL + word
        data = requests.get(fullURL).text
        soup = BeautifulSoup(data, 'html.parser')
        news_title = soup.find_all(class_='_sp_each_title')
        title_array = []
        for title in news_title:
            title_array.append({'url':title.get('href'), 'title':title.get('title')})
        context = {}
        context['form'] = form
        context['search_term'] = word
        context['object_list'] = title_array
        return render(self.request, self.template_name, context)