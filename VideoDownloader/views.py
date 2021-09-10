from django.shortcuts import redirect, render
from pytube import YouTube
from django.contrib import messages
# Create your views here.
def convert(url):
    yt = YouTube(url)
    yt.streams.get_by_resolution('360p').download("C:\\Users\\Administrator\\Desktop\\ourprojectdownloader")



def index(request):
    if request.method == "POST":
        print(request.POST['url'])
        url = request.POST['url']
        convert(url)
        messages.info(request,"Your File is Downloaded Successfully...")
        return redirect('/')
    else:
        return render(request,"index.html",{})