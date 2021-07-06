from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from restapi_board_app.util.paging import paging
import requests
import json
import datetime

# Create your views here.
class Notice(View):
    def get(self, request):
        list_url = 'http://localhost:8000/notices/all/'
        resDict = requests.post(list_url, data={'queryString':'SELECT * FROM t_board WHERE 1=1 ORDER BY rgst_dttm DESC'})
        resDict = resDict.text
        resDict_list = resDict.replace("}{","}?,/{").split("?,/")
        tmpResDict = list()

        for value in resDict_list:
            tmpResDict.append(eval(value))

        resDict_list = paging(request, tmpResDict)

        return render(request, 'notice.html', {'resDict_list':resDict_list})

class Notice_Detail(View):
    def post(self, request):
        list_url = 'http://localhost:8000/notices/details/'
        queryString = 'SELECT * FROM t_board WHERE 1=1 AND brd_uid =' + request.POST.get('brd_uid')
        resDict = requests.post(list_url, data={'queryString': queryString})
        resDict = resDict.text
        resDict_list = resDict.replace("}{","}?,/{").split("?,/")
        tmpResDict = list()

        for value in resDict_list:
            tmpResDict.append(eval(value))

        resDict = tmpResDict

        return render(request, 'noticeDetail.html', {'resDict':resDict})

class Notice_Write(View):
    def get(self, request):
        return render(request, 'noticeWrite.html', {})

class Notice_Write_Action(View):
    def post(self, request):
        list_url = 'http://localhost:8000/notices/write/'
        title = request.POST.get('title')
        cntnt = request.POST.get('cntnt')
        rgst_dttm = datetime.datetime.now()
        
        queryString = f"INSERT INTO t_board (title, cntnt, rgst_dttm) VALUES ('{title}','{cntnt}','{rgst_dttm}')"
        response = requests.post(list_url, data={'queryString': queryString})

        if(response.status_code == 200):
            resDict = json.dumps({'resCd' : '0000', 'mem_id' : '', 'JSON' : 'Y', "resMsg" : "[삭제] 정상처리 되었습니다."})
        else:
            resDict = json.dumps({'resCd' : '0203', 'mem_id' : '', 'JSON' : 'Y', "resMsg" : "[삭제] 정상처리 되었습니다."})

        print(resDict)

        return HttpResponse(resDict)