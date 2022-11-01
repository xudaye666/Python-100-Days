from django.db import models


class CarRecord(models.Model):
    carno = models.CharField(max_length=7)
    reason = models.CharField(max_length=50)
    date = models.DateTimeField(db_column='happen_date', auto_now_add=True)
    punish = models.CharField(max_length=50)
    isdone = models.BooleanField(default=False)

    @property
    def happen_date(self):
        return self.date.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        db_table = 'tb_car_record'
        ordering = ('-date', )
