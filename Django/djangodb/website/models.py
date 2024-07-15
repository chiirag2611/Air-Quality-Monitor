from django.db import models



class DataItem(models.Model):
    Timestamp = models.DateField(primary_key=False)
    CCS811_eCO2_ppm = models.IntegerField()
    CCS811_Tvoc_ppm = models.IntegerField()
    SCD41_CO2_ppm = models.IntegerField()
    SCD41_Temp_mC = models.IntegerField()
    SCD41_Humidity_mRH = models.IntegerField()
    SPS30_Pm2_5 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Timestamp
