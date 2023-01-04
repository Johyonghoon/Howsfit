from django.db import models


class Review(models.Model):
    use_in_migrations = True
    size_id = models.CharField(primary_key=True, unique=True)
    tow_piece_length = models.IntegerField()
    front_length = models.IntegerField()
    shoulder_length = models.IntegerField()
    sleeve_length = models.IntegerField()

    product_id = models.ForeignKey(Products, on_delete=model.CASCADE)  # TODO : PK Package 명으로 변경 필요

    class Meta:
        db_table = "review"

    def __str__(self):
        return f"{self.pk} {self.tow_piece_length} {self.front_length} " \
               f"{self.shoulder_length} {self.sleeve_length} {self.product_id}"
