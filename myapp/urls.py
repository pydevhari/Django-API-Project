# from .views import HomePageView
from django.urls import path
from .views import Insertdata


urlpatterns = [
    path('', Insertdata.display_page, name="page"),
    # path('display_data', Insertdata.get_data),
    path('insert_data', Insertdata.insert_data, name='insert_data'),
    path('fetch_result', Insertdata.fetch_result_data, name='insert_data'),
    path('get_result', Insertdata.get_result),
    path('admission', Insertdata.admission),
    path('insert_addmision_data', Insertdata.insert_addmision_data),
    path('delete_student', Insertdata.delete_student),
    path('delete_stu', Insertdata.delete_stu),
    path('update_detail', Insertdata.update_detail),
    path('update_verify', Insertdata.update_verify),
    path('update_action', Insertdata.update_action),
    # path('display_data')
    # path('home', HomePageView.as_view(), name='home'),
    # path('new_post', CreatePostView.as_view(), name='new_post'),
    # path('add_like/<int:pk>', addlike , name='add_like'),
    # path('postplus/', PostPlus.as_view() , name='post_plus'),
    # path('rest_login/', login_rest , name='login_rest'),
]
