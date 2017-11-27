from django.http import HttpResponse
from django.template import loader


def index(request):
   template = loader.get_template("about/index.html")
   return HttpResponse(template.render({}, request))

def project(request):
    return HttpResponse("<h2>The project is a sentimental analysis of depression rates over various countries</h2>"
                        "<p> It uses the following</p>"
                        "<li>D3 : <href>https://d3js.org/</href></li>"
                        "<li>Twitter Stream API : <href>https://www.npmjs.com/package/twitter-stream-api</href></li>"
                        "<li>Django 1.11 :<href>https://docs.djangoproject.com/en/1.11/</href></li>"
                        "<li>Sentimental analysis:<href></li>")

