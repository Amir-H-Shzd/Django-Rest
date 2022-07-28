from django.urls import path
from mysite.views import Home_view,About_view,Contact_view
urlpatterns = [
    # path('url address' , function in views , name)
    path('', Home_view),
    path('about/' , About_view),
    path('contact/' , Contact_view)
]