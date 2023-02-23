from cgitb import reset
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def testpaper(request):
    q=" Que-1::Who Developed C language?"
    a="Dennis M. Ritchie"
    b="Bjanrne Stroutrup"
    c="Guido van Rossum"
    d="James Gosling"
    d1={'que':q,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exame/test_paper.html',d1)
    return res
def testresult(request):
    s="<h1>testresult is shown<h1>"
    return HttpResponse(s)
