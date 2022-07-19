from django.urls import path
from mysite.views import Home_view,About_view,Contact_view
urlpatterns = [
    # path('url address' , function in views , name)
    path('', Home_view),
    path('About/' , About_view),
    path('Contact/' , Contact_view)
]