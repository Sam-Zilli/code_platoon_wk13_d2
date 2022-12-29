## polls/urls.py
from django.urls import path
from . import views

# In our urls.py, we namespaced our app with app_name 
# so that when we say polls:detail, there is no doubt about which app is
#  using the named route detail. Remember that a Django project can have many
#  apps and that one of those other apps could have detail. With polls:detail, 
# there is no doubt of which route we're using. For detail specifically, the
#  route is /polls/<int:question_id>. We are passing that id number into the
#  named route so that it automatically populates the URL.
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]