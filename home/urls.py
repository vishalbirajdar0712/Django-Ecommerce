from django.urls import path
from .views import index,test,about,contact,catwise_product,search
app_name = 'home'
urlpatterns = [

    path('',index,name='index'),
    path('test/',test),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('category/<int:id>/<slug:slug>',catwise_product,name='catwise_product' ),
    path('search/',search,name='search'),

]
