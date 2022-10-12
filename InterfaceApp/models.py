from django.db import models

class PerformanceList(models.Model):
    seq = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    startDate = models.IntegerField()
    endDate = models.IntegerField()
    place = models.CharField(max_length=50)
    realmName = models.CharField(max_length=10)
    area = models.CharField(max_length=10, null=True)
    thumbnail = models.CharField(max_length=256)
    gpsX = models.DecimalField(null=True)
    gpsY = models.DecimalField(null=True)

    def __str__(self):
        return f"seq: {self.seq}, title: {self.title}, startDate: {self.startDate}, endDate: {self.endDate}, place: {self.place}, realmName: {self.realmName}, area: {self.area}, thumbnail: {self.thumbnail}, gpsX: {self.gpsX}, gpsY: {self.gpsY}"

