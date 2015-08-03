from django.db import models

# Create your models here.
class SignUp(models.Model):
    class Meta:
        db_table = 'sign_up'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def full_name(self):
        return self.first_name + ' ' + self.last_name
    full_name.short_description = "Full name"

    def __unicode__(self):
        return self.email
