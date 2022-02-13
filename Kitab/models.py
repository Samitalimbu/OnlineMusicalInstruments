from django.db import models


# Create your models here.
class kitab(models.Model):

    kitab_id=models.AutoField(auto_created=True,primary_key=True)

    kitab_name=models.CharField(max_length=200)


    kitab_fromthePublisher=models.CharField(max_length=200)

    kitab_abouttheAuthor=models.CharField(max_length=200)

   

    Kitab_product_Details=models.CharField(max_length=800)

    Kitab_image=models.FileField(upload_to='Kitab_image')

   

    class Meta:

        db_table="Kitab"

class Booking(models.Model):

    Mbooking_id=models.AutoField(auto_created=True,primary_key=True)

    product_name=models.ForeignKey(kitab,on_delete=models.CASCADE)

    your_name=models.CharField(max_length=100)

    address=models.CharField(max_length=100)

    date = models.DateField()

    phone_number=models.CharField(max_length=50)

    location=models.CharField(max_length=100)




    class Meta:

        db_table="boking_musicalInstruments"
         
