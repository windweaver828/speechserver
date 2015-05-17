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
        response = "Recognition Failed " + sentence
    else:
        func, args = output
        line = "{func}(".format(func=repr(func).split()[1])
        if args:
                line += ", ".join(repr(arg) for arg in args)
        line += ')'
        output = callCommand(*output)
        response = "Recognition Success " + line

    return HttpResponse(response)
