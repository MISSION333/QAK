import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import re
from main import utils
from main import models


def index(request):
    return render(request, "index.html", {})


def blog_list(request):
    context = {}
    blogs = models.Blog.objects.all()

    context["blogs"] = blogs


    return render(request, "blog_list.html", context)


def blog_detail(request, blog_id):
    context = {}

    blog = get_object_or_404(models.Blog, pk=blog_id)
    context["blog"] = blog
    # print(blog.sections.all())
    context["sections"] = blog.sections.all()

    # for section in blog.sections:
    #     section.title, section.content

    return render(request, "blog.html", context)





def prompt(request):
    context = {}
    return render(request, "prompt.html", context)


def genrator(request):
    # context = {}
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecoderError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        x = utils.prompt_openai(data.get("question"))
        # Remove ,} from text to go parse to json
        regex = r",(\s)*}"
        replacment = "}"
        text_in = x.get("choices")[0].get("message").get("content").replace("\n", "")
        ready_to_parse = re.sub(regex, replacment, text_in)

        try:
            data = json.loads(ready_to_parse)
            blog = models.Blog(title=data["Title"])
            blog.save()
            for id, section in enumerate(data["Sections"]):
                models.Section.objects.create(title=section["SectionTitle"], content=section["SectionContent"], blog=blog)

            return JsonResponse(data)

        except json.decoder.JSONDecodeError:
            print(ready_to_parse)
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
            # context["data"] = ready_to_parse
            # return render(request, "generate.html", context)

        # return JsonResponse(data)
        # return JsonResponse({"Oh":"No"})
        # context["question"] = question
        # x = utils.prompt_openai(question, model="gpt-4")
        # context["data"] = x.get("choices")[0].get("message").get("content").replace("\n", "")
        # context["data"] = json.loads(x.get("choices")[0].get("message").get("content").replace("\n", "").replace("    ","").replace(",}", "}"))
        # print(context["data"])





