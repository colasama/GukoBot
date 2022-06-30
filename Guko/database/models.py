from datetime import datetime

from tortoise import fields
from tortoise.models import Model


class Nickname(Model):
    user_id = fields.IntField()
    nickname = fields.TextField()
