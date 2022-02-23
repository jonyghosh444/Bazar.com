from django.db import models

# Create your models here.


class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    head0 = models.CharField(max_length=300, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=300, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=300, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    Thumbnail = models.ImageField(upload_to='blog/image', default="")

    def __str__(self):
        details = f"{self.post_id} - {self.title}"
        return details