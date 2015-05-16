from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the speech home page.")

def speech(request, sentence):
    response = "You said: {}".format(sentence)
    return HttpResponse(response)
