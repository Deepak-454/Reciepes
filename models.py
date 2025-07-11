from django.db import models
class Receipes(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    receipe_name=models.CharField(max_length=50)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to="receipeimage",null=True,blank=True) # add receipeimage file in public/static folder
