from django.db import models


class ServiceRequest(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.username + ' - ' + self.type+ ' - ' + self.status 
    

