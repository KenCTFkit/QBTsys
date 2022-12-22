from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# モデルクラスを作成
class User(models.Model):
	# 項目定義
    StudentID     = models.CharField(max_length=6)
    TemperatureA    = models.IntegerField(validators=[MinValueValidator(32), MaxValueValidator(42)])
    TemperatureB    = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    Q1 = models.BooleanField()
    Q2  = models.BooleanField()
    FreeText = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # テキスト表示
# Create your models here.
