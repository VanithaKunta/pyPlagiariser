from django.conf.urls import url
from . import views
from . import sample_page3
from . import mainprog
urlpatterns=[

    url(r'^$',views.add,name='add'),
    url(r'file2/$',views.add2,name='add2'),
    url(r'file2/result/$',mainprog.percent,name='getresult')
]