from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the speech home page.")


def speech(request, inpsentence):
    from commander.Commands import commands
    from commander.commandtools import matchCommand, callCommand
    from commander.utilities import numToWords
    sentence = []
    for word in inpsentence.lower().split():
        try:
            word = numToWords(int(word))
        except:
            pass
        sentence.append(word)

    sentence = ' '.join(sentence)

    output = matchCommand(sentence, commands)
    if not output:
        response = "Recognition Failed"
    else:
        stderr, stdout = callCommand(*output)
        response = "Recognition Success {} {}".format(stdout, stderr)

    return HttpResponse(response)
