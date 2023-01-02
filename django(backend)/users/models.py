from django.db import models

class Users(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=120)
    passwd = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    birthday = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    phone_number = models.IntegerField()

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.id} {self.email} {self.passwd} {self.name} ' \
               f'{self.birthday} {self.height} {self.weight} {self.phone_number}'