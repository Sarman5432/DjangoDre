from django.db import models

FIGHTER_TYPE_CHOICES = [(0, "Water"), (1, "Earth"), (2, "Fire"), (3, "Air")]

# Model = where we work with sql/database but as a object. 
# So create the "schema" for the fighter object/class. Makes a table with these columns/fields
# These are the parameters the front end will work with for get/post etc


class Fighter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)  
    description = models.CharField(max_length=100, blank=True) #blank=true, means we can have a empty string as valid
    health = models.IntegerField()
    attack = models.IntegerField()
    speed = models.IntegerField()
    fighter_type = models.IntegerField(choices=FIGHTER_TYPE_CHOICES)  #can only be one of the predefined values. Strings of tuple are not stored in database, only numbers. Strings are shown during debugging
    weakness = models.IntegerField(choices=FIGHTER_TYPE_CHOICES)
    image = models.ImageField(upload_to="media", null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)  #auto assign date to current time

    # extra meta data. All data will be order from newest to oldest based on datetime_created property
    class Meta:
        ordering = ["-datetime_created"]
