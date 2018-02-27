from django.http import HttpResponse



def indexo(request):
    return HttpResponse("<h1>How I implemented ML</h1>"
                        "<p>I started off with the Andrew NG introductry videos on coursera : <a href>https://www.coursera.org/learn/machine-learning/home/welcome</href></a></p>"
                        "<p>It helps in getting the basics of Machine learning clear and strong</p>"
                        "<p>Here's a list of important algorithms</p>"
                        "<li>NAIVE BAYES </li>"
                        "<li>K-MEANS</li>"
                        "<li>SUPPORT VECTOR MACHINES</li>"
                        "<li>LINEAR REGRESSION</li>"
                        "<li>LOGISTIC REGRESSION</li>"
                        "<li>RANDOM FORESTS</li>"
                        "<li>DECISION TREES</li>"

                                              )
