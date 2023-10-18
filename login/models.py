from django.db import models

# Create your models here.

class User(models.Model):
    fullName = models.CharField(max_length=255)
    room = models.CharField(max_length=20)
    dateOfBirth = models.DateField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Người dùng"

class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField("logined time")
    status = models.CharField(max_length=255)
    imageUrl = models.CharField(max_length=255)
    modelId = models.IntegerField()

    class Meta:
        verbose_name_plural = "Lịch sử đăng nhập"
