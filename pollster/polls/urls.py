from django.urls import path

from . import views 

app_name = 'polls'
urlpatterns = [
    #empty path concatenates with whatever is the path in urls.py in pollster
    #/polls in this case 
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>', views.results, name='results')
]
