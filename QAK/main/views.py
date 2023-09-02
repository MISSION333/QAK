import json
from django.http import JsonResponse
from django.shortcuts import render
import re
from main import utils

def index(request):
    context = {}
    return render(request, "index.html", context)

# def genrator(request):
#     context = {}
#     if request.method == "POST":
#         print(request.POST)
#         question = request.POST.get("question")
#         context['question'] = question
#         # p = utils.prompt_cohere(question)
#         # context['text'] = p[0].text
#         text = utils.prompt_llama2(question)
#         context['text'] = text
#     # response[0].prompt, response[0].text
#     return render(request, "generate.html", context)

def regex_a(regex, replacment, text_in):
    # regex = r",(\s)*}"
    # replacment = "}"
    # text_in = x.get("choices")[0].get("message").get("content").replace("\n", "")
    return re.sub(regex, replacment, text_in)


def genrator(request):
    context = {}
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecoderError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

        # return JsonResponse(data)

    # return JsonResponse({"Oh":"No"})

        # context["question"] = question
        # x = utils.prompt_openai(question, model="gpt-4")
        x = utils.prompt_openai(data.get("question"))
        context["data"] = x.get("choices")[0].get("message").get("content").replace("\n", "")
        context["data"] = json.loads(x.get("choices")[0].get("message").get("content").replace("\n", "").replace("    ","").replace(",}", "}"))

        # Remove ,} from text to go parse to json
        regex = r",(\s)*}"
        replacment = "}"
        text_in = x.get("choices")[0].get("message").get("content").replace("\n", "")
        ready_to_parse = re.sub(regex, replacment, text_in)

        try:
            context["data"] = json.loads(ready_to_parse)
            return JsonResponse(context["data"])
        except json.decoder.JSONDecodeError:
            print(ready_to_parse)
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
            # context["data"] = ready_to_parse
            # return render(request, "generate.html", context)

        # print(context["data"])





