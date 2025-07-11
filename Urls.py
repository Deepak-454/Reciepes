# add this to url patterns
urlpatterns=[path('receipes/',receipes,name="reciepes"),
    path('delete_receipe/<id>/',delete_receipe,name="delete_receipes"),
    path('update_receipe/<id>/',update_receipe,name="update_receipe"),
    path('login/',login_page,name="login"),
    path('logout/',logout_page,name="logout"),
    path('Register/',register,name="register")]
