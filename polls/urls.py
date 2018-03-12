from django.conf.urls import url

from . import views

# regex or regular expressions, used to dynamically scrape pages for information you're looking for
# r'' contains the expressions used to filter through data
# ^ matches start of a string
# ?P<name> in parentheses allows this whole group to then have other regexs applied after them
# [0-9] looks for a digit between 0 and 9
# + looks for one or more occurences, in this case one or more occurences of a digit between 0 and 9
# / is not a special character in regex so this is simply looking for a /
# $ matches the end of a string
# next input is what variable the regex is looking in

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
