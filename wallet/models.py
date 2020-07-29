from django.db import models
# Create your models here.

class UserProfileInfo(models.Model):

    portfolio = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add = True,editable=True)
    joker = models.CharField(max_length=100,blank = True)
    balance = models.PositiveIntegerField()

    def finder(self,usern):
        print(self.user.username)
        if(self.user.username==usern):
            return True
        else:
            return False

    def __str__(self):
        return str(self.user)
