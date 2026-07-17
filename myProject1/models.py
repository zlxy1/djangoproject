from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class Staff(models.Model):
    # 基础信息
    name = models.CharField(max_length=20, verbose_name="员工姓名")
    GENDER_CHOICES = [("M","男"),("F","女")]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="性别")
    id_card = models.CharField(max_length=18, unique=True, verbose_name="身份证号")
    phone = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    birth = models.DateField(verbose_name="出生日期")
    address = models.CharField(max_length=200, blank=True, verbose_name="住址")

    # 模型配置内部类
    class Meta:
        # 新增/编辑页标题
        verbose_name = "员工"
        # 列表页、侧边菜单标题
        verbose_name_plural = "员工信息"
        # 默认按入职时间倒序（新员工在前）
        ordering = ["-id"]