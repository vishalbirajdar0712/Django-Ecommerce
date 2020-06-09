from django.urls import path
from .views import product,show_genres

app_name = 'products'
urlpatterns = [
    path('<int:id>/<slug:slug>',product,name = 'product'),

path('genre/',show_genres),
# path('category/<int:id>/<slug:slug>',catwise_product,name='category_product' ),
]
