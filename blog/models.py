from django.db import models
from django.utils import timezone
#lines with 'from' and 'import' add things from other files

class Post(models.Model): # defines the model (it is an object)
#'class' indicates that we are defining an object
#'Post' is the name of the model
#models.Model indicates that it is a Django model, so Django knows to store it in the database
    author = models.ForeignKey('auth.User')#ForeignKey=link to another model
    title = models.CharField(max_length=200)#Charfield=define text with limited number of characters
    text = models.TextField()#TextField=long text with no limit
    created_date = models.DateTimeField(#date and time
        default=timezone.now)
    pubished_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        #use lowercase and underscores as spaces when naming things
    def __str__(self):
        return self.title
        #indent the methods with the class OR ELSE
