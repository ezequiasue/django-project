# type:ignore
from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [

    # Homepage
    path('', views.dashboard, name='dashboard'),

    # List Lacamentos
    path('listall', views.listall, name='listall'),
    path('search', views.search, name='search'),


    # Lancamento (CRUD)
    path('lancamento/<int:lancamento_id>/', views.lancamento, name='lancamento'),  # noqa E501
    # Add Lancamento
    path('add', views.add_lancamento, name='add_lancamento'),

    path('edit', views.edit_lancamento, name='edit_lancamento'),
    path('update/<str:id>', views.update_lancamento, name='update_lancamento'),
    path('delete/<str:id>', views.delete_lancamento, name='delete_lancamento'),  # noqa 501

]
