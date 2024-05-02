# from .views import create_interns_from_json
from django.urls import path
from . import views

urlpatterns = [
    # path('read-and-store-data/', create_interns_from_json, name='create_interns_from_json'),
    path('internship/', views.list_Internship),
    path('internship/create/', views.create_Internship),
    path('internship/<int:internship_id>/', views.retrieve_Internship),
    path('internship/<int:internship_id>/update/', views.update_Internship),
    path('internship/<int:internship_id>/delete/', views.delete_Internship),
    path('start_scraping/<int:internship_id>/', views.start_scraping),
    path('interns/', views.intern_list),
    path('interns/<int:pk>/', views.intern_detail),
    path('all_Internship_Interns/<int:Internship_id>/', views.all_Internship_Interns),
    path('user_code_view/', views.user_code_view, name='user_code_view'),



]