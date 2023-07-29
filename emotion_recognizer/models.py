from django.db import models


def get_upload_to(instance, filename):
    return '%s/%s' % (instance.user_id, filename)


class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    

class File(models.Model):
    file_upload = models.FileField(upload_to=get_upload_to)
    user_id = models.BigIntegerField(models.ForeignKey("app.User", on_delete=models.CASCADE), unique=True)
    
    def delete(self, *args, **kwargs):
        self.file_upload.delete()
        super().delete(*args, **kwargs)
    