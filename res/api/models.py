from django.db import models
from django.core.validators import RegexValidator


# Create your Model here.
class Required(models.Model):
    name =models.CharField(max_length=39)
    email_id=models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$',
                                 message="Phone number must be entered in the format: '+919999999'. Up to 11 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators sh

    city=models.CharField(max_length=22)
    responsiblity=models.TextField(default=True,max_length=200)
    be_cgpa = models.CharField(max_length=4)
    hsc_percent = models.CharField(max_length=5)
    ssc_percent = models.CharField(max_length=5)
    #skilling = models.CharField(max_length=30)
  #  skilling =






#class Skiller(models.Model):
 # skill = models.ForeignKey(Required,on_delete=models.CASCADE)


