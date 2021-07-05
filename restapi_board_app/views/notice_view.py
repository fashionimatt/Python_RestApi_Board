from django.shortcuts import render
from django.views import View
import requests
import json

# Create your views here.
class Notice(View):
    def get(self, request):
        list_url = 'http://localhost:8000/index/notice/'
        jsonResponse = requests.post(list_url, data={'queryString':'SELECT * FROM t_board WHERE 1=1 ORDER BY updt_dttm DESC'})

        print("-----------------------")
        print(jsonResponse)
        print("-----------------------")
        print(jsonResponse.headers)
        print("-----------------------")
        print(jsonResponse.text)
        print("-----------------------")
        print(jsonResponse.text.replace("[", ""))
        print("-----------------------")
        
        for p in jsonResponse:
            print(p.title)

        return render(request, 'notice.html', {'jsonResponse':jsonResponse})