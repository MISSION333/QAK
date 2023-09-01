from django.shortcuts import render
from main import utils

# > from django.http import JsonResponse
# >>> response = JsonResponse({"foo": "bar"})


def index(request):
    context = {}
    return render(request, "index.html", context)


def genrator(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        question = request.POST.get("question")
        context['question'] = question
        # p = utils.prompt_cohere(question)
        # context['text'] = p[0].text

        text = utils.prompt_llama2(question)
        context['text'] = text


    # response[0].prompt, response[0].text
    return render(request, "generate.html", context)
