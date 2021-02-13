from django.urls import path

from . import views

app_name = 'finances'
urlpatterns = [
    path('statements/', views.statements, name='statements'),
    path('<int:statement_id>/transactions', views.transactions, name='transactions'),
    path('categories/', views.categories, name='categories'),
    path('<int:category_id>/expressions', views.expressions, name='expressions')
]
