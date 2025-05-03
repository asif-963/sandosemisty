from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.index, name= 'index'),
  path('about', views.about, name= 'about'),
  path('deluxe-room', views.deluxe_room, name= 'deluxe_room'),
  path('suite-room', views.suite_room, name= 'suite_room'),


  path('nearby-place/', views.near_by_place, name='near_by_place'),
  path('nearby-place/<int:place_id>/', views.near_by_place_details, name='near_by_place'),
  path('our-gallery', views.our_gallery, name= 'our_gallery'),
  path('gallery/<int:folder_id>/', views.gallery, name= 'gallery'),
  path('contact', views.contact, name= 'contact'),
  path('booking', views.booking, name= 'booking'),












      # Admin Login
    path('login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),

    # admin dashboard
    path('dashboard',views.dashboard,name='dashboard'),

     # Contact us
    path('contact_view',views.contact_view,name='contact_view'),
    path('delete_contact/<int:id>/',views.delete_contact,name='delete_contact'),

      # Booking
    path('booking_view',views.booking_view,name='booking_view'),
    path('delete_booking/<int:id>/',views.delete_booking,name='delete_booking'),


    # NEar By Place
    path('add_near_by_place', views.add_near_by_place, name='add_near_by_place'),
    path('view_near_by_place',views.view_near_by_place,name='view_near_by_place'),
    path('update_near_by_place/<int:id>/',views.update_near_by_place,name='update_near_by_place'),
    path('delete_near_by_place/<int:id>/',views.delete_near_by_place,name='delete_near_by_place'),

    path('ckeditor_upload/', views.ckeditor_upload, name='ckeditor_upload'),

    # client reviews
    path('add_client_review',views.add_client_review,name='add_client_review'),
    path('view_client_reviews',views.view_client_reviews,name='view_client_reviews'),
    path('update_client_review/<int:id>/',views.update_client_review,name='update_client_review'),
    path('delete_client_review/<int:id>/',views.delete_client_review,name='delete_client_review'),

     # Add Folders
    path('add_folders', views.add_folders, name='add_folders'),
    path('view_folders',views.view_folders,name='view_folders'),
    path('update_folder/<int:id>/',views.update_folder,name='update_folder'),
    path('delete_folder/<int:id>/',views.delete_folder,name='delete_folder'),

     # Add Images
    path('add_images', views.add_images, name='add_images'),
    path('view_images',views.view_images,name='view_images'),
    path('update_image/<int:id>/',views.update_image,name='update_image'),
    path('delete_image/<int:id>/',views.delete_image,name='delete_image'),


    # add PRice
    path('add-price', views.add_price, name='add_price'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'sandose_misty_app.views.page_404'