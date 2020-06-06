from django.db import models


class Registers(models.Model):
        stname=models.CharField(max_length=100)
        branch=models.CharField(max_length=100)
        year=models.CharField(max_length=100)
        mn = models.CharField(max_length=10)
        rno=models.IntegerField()
        remail = models.EmailField(max_length=100)
        passs=models.CharField(max_length=100)
        cpass=models.CharField(max_length=100)
        def __str__(self):
            return self.stname

class gdt(models.Model):
        stname = models.CharField(max_length=100)
        branch = models.CharField(max_length=100)
        year = models.CharField(max_length=100)
        mn = models.CharField(max_length=10)
        rno = models.IntegerField()
        gemail = models.EmailField(max_length=100)
        gdate=models.CharField(max_length=100)
        gtime = models.CharField(max_length=100)
        passs = models.CharField(max_length=100)
        cpass = models.CharField(max_length=100)
        def __str__(self):
                return self.stname
class pptt(models.Model):
        stname = models.CharField(max_length=100)
        branch = models.CharField(max_length=100)
        year = models.CharField(max_length=100)
        mn = models.CharField(max_length=10)
        rno = models.IntegerField()
        pdate=models.CharField(max_length=100)
        pemail = models.EmailField(max_length=100)
        ptime = models.CharField(max_length=100)
        ppttopic = models.CharField(max_length=100)
        passs = models.CharField(max_length=100)
        cpass = models.CharField(max_length=100)
        def __str__(self):
                return self.stname
class notification(models.Model):
        adminnotice=models.CharField(max_length=100)
        def __str__(self):
                return self.adminnotice

class judge(models.Model):
        stname = models.CharField(max_length=100)
        branch = models.CharField(max_length=100)
        year = models.CharField(max_length=100)
        cc = models.CharField(max_length=100)
        ef= models.CharField(max_length=100)
        co = models.CharField(max_length=100)
        rt = models.CharField(max_length=100)
        total = models.IntegerField()
        def __str__(self):
                return self.stname

class win(models.Model):
        stname = models.CharField(max_length=100)
        year = models.CharField(max_length=100)
        branch = models.CharField(max_length=100)
        rank = models.CharField(max_length=100)
        def __str__(self):
                return self.stname