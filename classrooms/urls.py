
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from classes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/github', views.test_api, name='test-api'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    path('classrooms/signin', views.signin, name='signin'),
    path('classrooms/<int:classroom_id>/student_create', views.student_create, name='student-create'),
    path('classrooms/<int:classroom_id>/<int:student_id>/student_update', views.student_update, name='student-update'),
    path('classrooms/<int:classroom_id>/<int:student_id>/student_delete', views.student_delete, name='student-delete'),

	path('classrooms/signout', views.signout, name='signout'),    
	path('classrooms/signup', views.signup, name='signup'),  

    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
