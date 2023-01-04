from django.db import models


class RecsBySize(models.Model):
    use_in_migrations = True
    recs_size = models.AutoField(primary_key=True, unique=True)

    user_id = models.ForeignKey(Users, on_delete=model.CASCADE)  # TODO : PK Package 명으로 변경 필요
    size_id = models.ForeignKey(Sizes, on_delete=model.CASCADE)  # TODO : PK Package 명으로 변경 필요
    product_id = models.ForeignKey(Products, on_delete=model.CASCADE)  # TODO : PK Package 명으로 변경 필요

    class Meta:
        db_table = "review"

    def __str__(self):
        return f"{self.pk} {self.user_id} {self.size_id} {self.product_id}"
