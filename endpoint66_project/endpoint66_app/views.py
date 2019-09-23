from django.http import HttpResponse

def index(request):
    return HttpResponse("gogetthegood")

def happyhappyjoyjoy(request):
    return HttpResponse("happyhappyjoyjoy")

def gogetthegood(request):
    return HttpResponse("gogetthegood")

# Create your views here.
