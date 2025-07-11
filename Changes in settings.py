# Enter the App Name in the list of INSTALLED_APPS
#Add this for media files
import os
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIR={
    os.path.join(BASE_DIR,"public/static")
}
MEDIA_ROOT=os.path.join(BASE_DIR,'public/static')
MEDIA_URL='/media/'
