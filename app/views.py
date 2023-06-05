from django.shortcuts import render

# Create your views here.
def app_htmlpage(request):
    d={'name':'Sudhanshu Pandey','age':23,'job':'Software Developer'}
    return render(request,'app_htmlpage.html',context=d)