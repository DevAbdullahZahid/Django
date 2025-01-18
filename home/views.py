from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable1': " This is First Variable",
        'variable2':"this is second variable",
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')
   # return HttpResponse("This is about page")


def service(request):
    return render(request, 'services.html')
    #return HttpResponse("This is Service page")
def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is Contact page")