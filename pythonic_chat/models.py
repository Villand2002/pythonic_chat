import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
# 部屋のモデル
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    

# メッセージのmodel
class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.ForeignKey(
        Room,
        blank=True,
        null=True,
        related_name='room_meesages',
        on_delete=models.CASCADE
    )
    # リレーション設定
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

# userのモデル
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    password = models.CharField(min_length=8)
    room=models.ManyToManyField(Room)
    message=models.ManyToManyField(Message)
    # 部屋とメッセージは多対多のリレーションとする.
    created_at = models.DateTimeField(default=timezone.now)
