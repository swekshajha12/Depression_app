from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is the college club homepage</h1>")
def project(request):
    return HttpResponse("<h2>The project is a sentimental analysis of depression rates over various countries</h2>"
                        "<p> It uses the following</p>"
                        "<li>D3 : <href>https://d3js.org/</href></li>"
                        "<li>Twitter Stream API : <href>https://www.npmjs.com/package/twitter-stream-api</href></li>"
                        "<li>Django 1.11 :<href>https://docs.djangoproject.com/en/1.11/</href></li>"
                        "<li>Sentimental analysis:<href></li>")
